# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 14:04:59 2020

@author: GOVINDA
"""
# Importing the importent libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

dataset=pd.read_csv('hiring.csv')

# fill nan value with 0 in experience fillna method of df
dataset['experience'].fillna(0,inplace=True)

# fill text_score nan value with mean of test_score
dataset['test_score'].fillna(dataset['test_score'].mean(),inplace=True)

# assign features column in variable X
X=dataset.iloc[:,:3]

# Converting words to integer for experience feature
def convert_to_int(word):
    word_dict={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'zero':0,0:0}
    return word_dict[word]

X['experience']=X['experience'].apply(lambda x: convert_to_int(x))
# predication variable
y=dataset.iloc[:,-1]

#Splliting Training and Test Set
#Since we have a very small dataset, we will train complete

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()

#Fitting model with training data
regressor.fit(X,y)

# Predict
#var=regressor.predict([[7,8,8]])

#Saving Model to disk
pickle.dump(regressor,open('model.pkl','wb'))
