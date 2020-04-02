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
import shutil
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def loadData():  
    panda_data = pandas.read_csv("malbecBrunello.csv",converters={
            "id":int,"price":float,"JS":float,"vintage":float,"malbec":float,"brunello":float})
    raw_wine_data = np.asarray(panda_data)
#    raw_wine_data = np.delete(raw_wine_data, (0), axis=0)
    raw_wine_data=raw_wine_data[:-15, :]
#    JS_scores = np.empty((len(raw_wine_data),4), dtype=np.float32)
#    JS_wines = np.empty((len(raw_wine_data),1), dtype=np.float32)
#    JS_scores.fill(np.delete(raw_wine_data,(0,1,2,3,5,6,7),axis=1))
#    JS_wines.fill(np.delete(raw_wine_data,(0,1,4,5),axis=1))
    JS_scores = np.delete(raw_wine_data,(0,1,2,3,5,6,7),axis=1)
    JS_wines = np.delete(raw_wine_data,(0,1,4,5),axis=1)
    
    JS_scores = JS_scores.astype(np.float32)
    JS_wines = JS_wines.astype(np.float32)
    
    return raw_wine_data, JS_wines, JS_scores
    
    
raw_wine_data, JS_wines, JS_scores = loadData()
if os.path.isdir(os.path.join(os.getcwd(), 'train')):
    shutil.rmtree('train')
print(raw_wine_data[69])

JS_wines = JS_wines / JS_wines.max(axis=0)
vintages=JS_wines[:,0]
prices=JS_wines[:,1]
malbecs=JS_wines[:,2]
brunellos=JS_wines[:,3]
x_dict= {'vintage':vintages,'price':prices,'malbec':malbecs,'brunello':brunellos}
FEATURES = ["vintage","price","malbec","brunello"]
LABEL = "JS"

#feature_cols = [tf.feature_column.numeric_column(k,normalizer_fn = tf.contrib.layers.batch_norm) for k in x_dict.keys()]	
feature_cols = [tf.feature_column.numeric_column(k) for k in x_dict.keys()]	

#JS_wine_dict = []
#
#for i in range(len(JS_scores)):
#    wine = {FEATURES[0]:JS_wines[i][0],FEATURES[1]:JS_wines[i][1],FEATURES[2]:JS_wines[i][2],FEATURES[3]:JS_wines[i][3]}
#    JS_wine_dict.append(wine)

#print(JS_wine_dict[0]["vintage"])

def get_input_fn(wines, scores, num_epochs=None, n_batch = 864, shuffle=True): 
    return tf.estimator.inputs.numpy_input_fn(       
         x= wines,       
         y = scores,       
         batch_size=n_batch,          
         num_epochs=num_epochs,       
         shuffle=shuffle)		

#estimator = tf.estimator.LinearRegressor(    
#        feature_columns=feature_cols,   
#        model_dir="train",
#        optimizer=lambda: tf.train.FtrlOptimizer(
#        learning_rate=tf.train.exponential_decay(
#            learning_rate=1.5,
#            global_step=tf.train.get_global_step(),
#            decay_steps=1000,
#            decay_rate=0.92)))

#estimator = tf.estimator.LinearRegressor(    
#        feature_columns=feature_cols,   
#        model_dir="train",
#        optimizer=lambda: tf.train.AdamOptimizer(learning_rate=0.005))
    
estimator = tf.estimator.LinearRegressor(    
        feature_columns=feature_cols,   
        model_dir="train",
        optimizer=lambda: tf.train.GradientDescentOptimizer(learning_rate=0.00075,),
        loss_reduction=tf.losses.Reduction.SUM_OVER_BATCH_SIZE)

estimator.train(input_fn=get_input_fn(x_dict, JS_scores),                                      
                                           steps=3000)
   


predict = estimator.predict(input_fn=get_input_fn(x_dict, JS_scores, num_epochs=1, n_batch = 864, shuffle=False))	

#print(next(predict))      
#classifier = tf.estimator.LinearClassifier(feature_columns=JS_wines)
#classifier.train(JS_wines)
#
#result = classifier.evaluate(JS_wines)

f = open('results_with_vintage.csv','w')
f.write('name,vintage,type,price,score,prediction,difference\n')  #Give your csv text here.
## Python will convert \n to os.linesep

for i in range(len(JS_scores)):
    guess = next(predict)['predictions'][0]
    if raw_wine_data[i][6]==1:
        wine_type = 'malbec'
    else:
        wine_type = 'brunello'
        
    f.write('%s,%d,%s,%.2f,%d,%.5f,%.5f\n' % (raw_wine_data[i][1],raw_wine_data[i][2],wine_type,raw_wine_data[i][3],JS_scores[i],guess,JS_scores[i]-guess))
#    print("%s %d: real: %d, guess: %f.3, diff: %f.3" % (raw_wine_data[i][1],raw_wine_data[i][2],JS_scores[i],guess,JS_scores[i]-guess))


f.close()