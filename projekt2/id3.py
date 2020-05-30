#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from data_input import DataReader
from math import log2
import pandas
import sys

MUSHROOMS = 8124
data = DataReader(0, MUSHROOMS, 0, 0, 'mushrooms/agaricus-lepiota.data')

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
        
        #stop condition
        if(self.features.empty):
            self.leaf = True
            self.label = self.labels.value_counts().idxmax()
            return
            
        #generate children
        attr = best_attribute(self.features,self.labels,self.exclude)
        
        #stop condition
        if(attr == ''):
            self.leaf = True
            self.label = self.labels.value_counts().idxmax()
            return
        
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
    def __init__(self, begin, end, begin2=0, end2=0):
        data = DataReader(begin, end, begin2, end2, 'mushrooms/agaricus-lepiota.data')
        self.features = data.get_features()
        self.labels = data.get_labels()
        self.root = ID3_Node(self.features, self.labels, list())
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

def test(tree, tests_begin, tests_end, results):
    j = tests_begin
    tests = tests_end - tests_begin
    correct = 0
    false_positive = 0
    false_negative = 0
    while j < tests_end:
        if tree.classify(j) == global_labels[j]:
            correct = correct + 1
        elif global_labels[j] == 'p':
            false_positive = false_positive + 1
        else:
            false_negative = false_negative + 1
        j = j + 1
    incorrect = false_positive + false_negative
    print("trained on: " + str(MUSHROOMS - tests) + ", performed " + str(tests) + " tests")
    print("\tcorrect: " + str(correct) + '/' + str(tests) + "({:.2f}".format(correct * 100 / tests) + "%)")
    print("\tincorrect: " + str(incorrect) + "({:.2f}".format(incorrect * 100 / tests) + "%)")
    print("\t\tfalse positives: " + str(false_positive) + '/' + str(tests) + "({:.2f}".format(false_positive * 100 / tests) + "%)")
    print("\t\tfalse negatives: " + str(false_negative) + '/' + str(tests) + "({:.2f}".format(false_negative * 100 / tests) + "%)")
    results['training set'].append(MUSHROOMS - tests)
    results['tests'].append(tests)
    results['correct'].append(correct)
    results['incorrect'].append(incorrect)
    results['false positives'].append(false_positive)
    results['false negatives'].append(false_negative) 
    return correct * 100 / tests

if __name__ == '__main__':
    print("taking mushrooms from top of file as training data, rest as tests")
    results = {'training set' : [], 'tests' : [], 'correct' : [], 'incorrect' : [], 'false positives' : [], 'false negatives' : []}
    for i in [float((x+1)/100) for x in range(90)]:
        training_data = int(MUSHROOMS * i)
        tree = ID3_Tree(0, training_data)
        test(tree, training_data + 1, MUSHROOMS, results)

    data_frame = pandas.DataFrame(data=results)
    data_frame.to_csv('results/results' + argv[1] + '.csv')

    print("cross validation - 3 iterations with 1/3 of mushrooms as tests")
    tests = int(MUSHROOMS / 3)
    tests_begin = 0
    correct = []
    for i in range(3):
        tests_end = tests_begin + tests
        tree = ID3_Tree(0, tests_begin, tests_end, MUSHROOMS)
        correct.append(test(tree, tests_begin, tests_end, results))
        tests_begin = tests_begin + tests
    average = sum(correct) / len(correct)
    print("cross validation - average accuracy: " + "{:.2f}".format(average) + "%")
    file = open("results/cross_validation.txt", "a")
    file.write(str(average) + "\n")