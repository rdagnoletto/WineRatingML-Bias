#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 01:57:59 2019

@author: ragnoletto
"""
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import time
import os
import sys
import scipy.io as sio
import pickle as pkl
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import csv
import pandas
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def loadData():    
    panda_data = pandas.read_csv("red_wine_filtered.csv",converters={
            "id":int,"price":float,"RP":int,"JS":int,"WE":int,"WS":int,"V":int,"vintage":int})
    raw_wine_data = np.asarray(panda_data)
#    raw_wine_data = np.delete(raw_wine_data, (0), axis=0)
    
    RP_wines = raw_wine_data[np.ix_(raw_wine_data[:,8] >1)]
    RP_scores = np.delete(RP_wines,(0,1,2,3,4,5,6,7,9,10,11,12,13),axis=1)
    RP_wines = np.delete(RP_wines,(9,10,11,12,13),axis=1)
    
    JS_wines = raw_wine_data[np.ix_(raw_wine_data[:,9] >1)]
    JS_scores = np.delete(JS_wines,(0,1,2,3,4,5,6,7,8,10,11,12,13),axis=1)
    JS_wines = np.delete(JS_wines,(9,10,11,12,13),axis=1)
    
    WE_wines = raw_wine_data[np.ix_(raw_wine_data[:,10] >1)]
    WE_scores = np.delete(WE_wines,(0,1,2,3,4,5,6,7,8,9,11,12,13),axis=1)
    WE_wines = np.delete(WE_wines,(9,10,11,12,13),axis=1)
    
    WS_wines = raw_wine_data[np.ix_(raw_wine_data[:,11] >1)]
    WS_scores = np.delete(WS_wines,(0,1,2,3,4,5,6,7,8,9,10,12,13),axis=1)
    WS_wines = np.delete(WS_wines,(9,10,11,12,13),axis=1)
    
    V_wines = raw_wine_data[np.ix_(raw_wine_data[:,12] >1)]
    V_scores = np.delete(V_wines,(0,1,2,3,4,5,6,7,8,9,10,11,13),axis=1)
    V_wines = np.delete(V_wines,(9,10,11,12,13),axis=1)
    
    return raw_wine_data, RP_wines, RP_scores, JS_wines, JS_scores, WE_wines, WE_scores, WS_wines, WS_scores, V_wines, V_scores
    
    
raw_wine_data, RP_wines, RP_scores, JS_wines, JS_scores, WE_wines, WE_scores, WS_wines, WS_scores, V_wines, V_scores = loadData()

