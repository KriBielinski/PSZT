#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:19:00 2020

@author: kristofer
"""

import pandas as pd

class DataReader:
    def __init__(self, begin, end, begin2=0, end2=0, filepath=None):
        
        self._names = ['edible','cap-shape','cap-surface','cap-color',
         'bruises','odor','gill-attachment','gill-spacing','gill-size',
         'gill-color','stalk-shape','stalk-root','stalk-surface-above-ring',
         'stalk-surface-below-ring','stalk-color-above-ring',
         'stalk-color-below-ring','veil-type','veil-color','ring-number',
         'ring-type','spore-print-color','population','habitat']
        
        self._data = pd.read_csv(filepath, header=None, 
                                 index_col=False, names=self._names)
        
        self._features = self._data.iloc[begin:end,1:].append(self._data.iloc[begin2:end2,1:])
        
        self._labels = self._data.iloc[begin:end,0].append(self._data.iloc[begin2:end2,0])
        
    
    def get_features(self):
        return self._features
    
    def get_labels(self):
        return self._labels