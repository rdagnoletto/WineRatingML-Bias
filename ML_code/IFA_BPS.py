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
import math
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def loadData():  
    panda_js = pandas.read_csv("IFA_BPS_JS_data.csv",converters={
            "id":int,"price":float,"JS":float,"vintage":float,"bordeauxBlends":float,"syrah":float,
            "pinot":float,"italy":float,"france":float,"australia":float})
    raw_js_data = np.asarray(panda_js)
    
    JS_scores = np.delete(raw_js_data,(0,1,2,3,5,6,7,8,9,10,11,12,13),axis=1) 
    JS_wines = np.delete(raw_js_data,(0,1,4,5,6,7),axis=1)
#    JS_wines_nv = np.delete(raw_js_data,(0,1,2,4,5,6,7),axis=1)
    
    JS_scores = JS_scores.astype(np.float32)
    JS_wines = JS_wines.astype(np.float32)
#    JS_wines_nv = JS_wines_nv.astype(np.float32)
    
    panda_rp = pandas.read_csv("IFA_BPS_RP_data.csv",converters={
            "id":int,"price":float,"RP":float,"vintage":float,"bordeauxBlends":float,"syrah":float,
            "pinot":float,"italy":float,"france":float,"australia":float})
    
    raw_rp_data = np.asarray(panda_rp)
    
    RP_scores = np.delete(raw_rp_data,(0,1,2,3,5,6,7,8,9,10,11,12,13),axis=1) 
    RP_wines = np.delete(raw_rp_data,(0,1,4,5,6,7),axis=1)
#    RP_wines_nv = np.delete(raw_rp_data,(0,1,2,4,5,6,7),axis=1)
    
    RP_scores = RP_scores.astype(np.float32)
    RP_wines = RP_wines.astype(np.float32)
#    RP_wines_nv = RP_wines_nv.astype(np.float32)
#    raw_wine_data = np.delete(raw_wine_data, (0), axis=0)
#    raw_wine_data=raw_wine_data[:-15, :]


    
    return raw_js_data, JS_wines, JS_scores, raw_rp_data, RP_scores, RP_wines
     

def train(name,wines,scores,feature_cols,raw_data,n_batch=None,steps=7000,learning_rate=0.001):
    if n_batch is None:
        n_batch = math.ceil(len(scores)/2)
    def get_input_fn(wines, scores, num_epochs=None, n_batch = 605, shuffle=True): 
        return tf.estimator.inputs.numpy_input_fn(       
             x= wines,       
             y = scores,       
             batch_size=n_batch,          
             num_epochs=num_epochs,       
             shuffle=shuffle)		
    
    
    estimator = tf.estimator.LinearRegressor(    
            feature_columns=feature_cols,   
            model_dir="train_ifa_bps/"+name,
            optimizer=lambda: tf.train.GradientDescentOptimizer(learning_rate=learning_rate,),
            loss_reduction=tf.losses.Reduction.SUM_OVER_BATCH_SIZE)
    
    estimator.train(input_fn=get_input_fn(wines, scores,n_batch=n_batch), steps=steps)
       
    
    predict = estimator.predict(input_fn=get_input_fn(wines, scores, num_epochs=1, n_batch = len(scores), shuffle=False))	
    # 0   1    2       3     4    5     6        7           8          9    10    11     12      13
    #id,name,vintage,price,score,url,varietal,location,bordeauxBlends,syrah,pinot,italy,france,australia    

#    f.write('name,vintage,varietal,location,price,score,prediction,difference,bordeauxBlends,syrah,pinot,italy,france,australia\n')
    with open('IFA_BPS_'+name+'_results.csv', 'w') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        csv_writer.writerow(['name','vintage','varietal','location','price','score','prediction',
                             'difference','bordeauxBlends','syrah','pinot','italy','france','australia'])
        for i in range(len(JS_scores)):
            guess = next(predict)['predictions'][0]
            csv_writer.writerow([str(raw_data[i][1]),str(raw_data[i][2]),str(raw_data[i][6]),
                        str(raw_data[i][7]),str(raw_data[i][3]),str(scores[i][0]),str(guess),str(scores[i][0]-guess),str(raw_data[i][8]),
                        str(raw_data[i][9]),str(raw_data[i][10]),str(raw_data[i][11]),str(raw_data[i][12]),str(raw_data[i][13])])
    #        f.write('%s,%d,%s,%s,%.2f,%d,%.5f,%.5f,%d,%d,%d,%d,%d,%d\n' % (raw_data[i][1],raw_data[i][2],raw_data[i][6],
    #                        raw_data[i][7],raw_data[i][3],scores[i],guess,scores[i]-guess,raw_data[i][8],
    #                        raw_data[i][9],raw_data[i][10],raw_data[i][11],raw_data[i][12],raw_data[i][13]))
    
    
    
raw_js_data, JS_wines, JS_scores, raw_rp_data, RP_scores, RP_wines = loadData()
if os.path.isdir(os.path.join(os.getcwd(), 'train_ifa_bps')):
    shutil.rmtree('train_ifa_bps')


JS_wines = JS_wines / JS_wines.max(axis=0)
RP_wines = RP_wines / RP_wines.max(axis=0)

x_JS = {'vintage':JS_wines[:,0],'price':JS_wines[:,1],'bordeauxBlends':JS_wines[:,2],'syrah':JS_wines[:,3],
       'pinot':JS_wines[:,4],'italy':JS_wines[:,5],'france':JS_wines[:,6],'australia':JS_wines[:,7]}
x_JS_nv = {'price':JS_wines[:,1],'bordeauxBlends':JS_wines[:,2],'syrah':JS_wines[:,3],
       'pinot':JS_wines[:,4],'italy':JS_wines[:,5],'france':JS_wines[:,6],'australia':JS_wines[:,7]}
x_RP = {'vintage':RP_wines[:,0],'price':RP_wines[:,1],'bordeauxBlends':RP_wines[:,2],'syrah':RP_wines[:,3],
       'pinot':RP_wines[:,4],'italy':RP_wines[:,5],'france':RP_wines[:,6],'australia':RP_wines[:,7]}
x_RP_nv = {'price':RP_wines[:,1],'bordeauxBlends':RP_wines[:,2],'syrah':RP_wines[:,3],
       'pinot':RP_wines[:,4],'italy':RP_wines[:,5],'france':RP_wines[:,6],'australia':RP_wines[:,7]}

features_JS = [tf.feature_column.numeric_column(k) for k in x_JS.keys()]	
features_JS_nv = [tf.feature_column.numeric_column(k) for k in x_JS_nv.keys()]	
features_RP = [tf.feature_column.numeric_column(k) for k in x_RP.keys()]	
features_RP_nv = [tf.feature_column.numeric_column(k) for k in x_RP_nv.keys()]	  

#name,wines,scores,feature_cols,raw_data,n_batch=None,steps=7000,learning_rate=0.001

#train("JS_v",x_JS,JS_scores,features_JS,raw_js_data,steps=7000,learning_rate=0.0012)

#train("JS_nv",x_JS_nv,JS_scores,features_JS_nv,raw_js_data,steps=7000,learning_rate=0.002)

#train("RP_v",x_RP,RP_scores,features_RP,raw_rp_data,steps=5000,learning_rate=0.00175)

#train("RP_nv",x_RP_nv,RP_scores,features_RP_nv,raw_rp_data,steps=7000,learning_rate=0.00275)
    
train("JS_v_long",x_JS,JS_scores,features_JS,raw_js_data,steps=30000,learning_rate=0.00075)

train("JS_nv_long",x_JS_nv,JS_scores,features_JS_nv,raw_js_data,steps=30000,learning_rate=0.00125)

train("RP_v_long",x_RP,RP_scores,features_RP,raw_rp_data,steps=30000,learning_rate=0.001)

train("RP_nv_long",x_RP_nv,RP_scores,features_RP_nv,raw_rp_data,steps=30000,learning_rate=0.0015)   