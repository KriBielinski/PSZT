#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from data_input import DataReader
from math import log2
import sys

MUSHROOMS = 8124
data = DataReader(MUSHROOMS, 'mushrooms/agaricus-lepiota.data')

global_features = data.get_features()
global_labels = data.get_labels()

def entropy(labels):
    label_count = len(labels)
    proportion_e = len(labels[labels == 'e'])/label_count
    proportion_p = len(labels[labels == 'p'])/label_count
    
    if(proportion_e == 0 or proportion_p == 0):
        #if all elements are of the same class then entropy = 0
        return 0
    
    return -proportion_e*log2(proportion_e)-proportion_p*log2(proportion_p)
    

def inf_gain(features, labels, atribute):
    entropy_offset = entropy(labels)
    
    for atribute_value in features[atribute].unique():
        labels_subset = labels[features[atribute]==atribute_value]
        subset_entropy = entropy(labels_subset)
        subset_proportion = len(labels_subset)/len(labels)
        
        entropy_offset -= subset_proportion*subset_entropy
    
    return entropy_offset

# returnes the best attribute to divide the data on based on information gain
def best_attribute(features, labels, exclude_attributes=[]):
    exclude_attributes = list(exclude_attributes)
    max_gain = -1
    best = ''
    for attribute in features.drop(exclude_attributes,axis=1).columns:
        gain = inf_gain(features, labels, attribute)
        if(gain > max_gain):
            max_gain = gain
            best = attribute
    return best


def divide_data(features, labels, attribute):
    sub_features_tab = []
    sub_labels_tab = []
    
    for attribute_value in global_features[attribute].unique():
        sub_features = features[features[attribute] == attribute_value]
        sub_labels = labels[features[attribute] == attribute_value]
        
        sub_features_tab.append(sub_features)
        sub_labels_tab.append(sub_labels)
    
    return sub_features_tab, sub_labels_tab

class ID3_Node:
    def __init__(self, features=None, labels=None, exclude_attributes=[]):
        self.features = features
        self.labels = labels
        #lista atrybutów których nie uwzględniamy w dzieleniu
        self.exclude = exclude_attributes
        self.children = list([])
        #atrybut względem którego ten node jest dzielony
        self.attribute = ''
        #wartość atrybutu dla którego ten node jest osiągany
        self.attr_value = ''
        #czy ten node jest liściem drzewa i jeżeli tak to jakiej jest klasy
        self.leaf = False
        self.label = ''
    
    def generate_children(self):
        
        #stop condition
        if(len(self.labels.unique()) == 1):
            self.leaf = True
            self.label = self.labels.unique()[0]
            return
        
        #if(self.features.empty):
        #    self.leaf = True
        #    self.label = self.labels.value_counts().idxmax()
        #    return
            
        #generate children
        attr = best_attribute(self.features,self.labels,self.exclude)
        self.exclude.append(attr)
        self.attribute = attr
        sub_features_tab, sub_labels_tab = divide_data(self.features,self.labels,attr)
        
        for i in range(len(sub_features_tab)):
            
            inode = ID3_Node(sub_features_tab[i], sub_labels_tab[i], self.exclude)
            inode.attr_value = global_features[attr].unique()[i]
            self.children.append(inode)
            
            #stop condition
            if(sub_features_tab[i].empty):
                inode.leaf = True
                inode.label = self.labels.value_counts().idxmax()
            else:
                inode.generate_children()
            
class ID3_Tree:
    def __init__(self, lines):
        data = DataReader(lines, 'mushrooms/agaricus-lepiota.data')
        self.features = data.get_features()
        self.labels = data.get_labels()
        self.root = ID3_Node(self.features, self.labels)
        self.root.generate_children()
    
    def print_structure(self):
        print('switch(' + self.root.attribute+'):')
        
        def print_children(root, n):
            for inode in root.children:
                if(inode.leaf):
                    print(n*'\t' + inode.attr_value + ': label(' + inode.label + ')')
                else:
                    print(n*'\t' + inode.attr_value + ': switch('+ inode.attribute+'):')
                    print_children(inode, n+1)
                    
        print_children(self.root, 1)

    def classify(self, index):
        root = self.root
        while root.leaf == False:
            for child in root.children:
                if child.attr_value == global_features[root.attribute][index]:
                    root = child
                    break
        return root.label


if __name__ == '__main__':
    if len(sys.argv) > 1:
        training_data = int(MUSHROOMS * int(sys.argv[1]) / 10)
        tree = ID3_Tree(training_data)
        j = training_data + 1
        correct = 0
        while j < MUSHROOMS:
            if tree.classify(j) == global_labels[j]:
                correct = correct + 1
            j = j + 1
        result = correct / (MUSHROOMS - (training_data + 1))
        print("trained on: " + str(training_data) + ", correct: " + str(result))