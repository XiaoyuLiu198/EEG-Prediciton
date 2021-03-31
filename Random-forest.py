#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 21:34:53 2020
"""
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

#Load sklearn
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import confusion_matrix

# Import Classifiers
from sklearn.ensemble import RandomForestClassifier



#read data and split
os.getcwd()
os.chdir('/Users/ruihuang/Downloads')
data = pd.read_csv('./complete1.csv')
del data['Unnamed: 0']
data.head()
del data['X']
y = data['agePeriod']
del data['age']
del data['agePeriod']
x = data
y.head()

# standardlize
min_max_scaler = preprocessing.MinMaxScaler()  
x_minMax = min_max_scaler.fit_transform(x)  
x_minMax

x_train, x_test, y_train, y_test = train_test_split(x_minMax,y,test_size=0.2,random_state=0,stratify=y)

x_train=pd.DataFrame(x_train)
x_train.head()


# a quick check the correlation
os.getcwd()
os.chdir('/Users/Downloads')
data1 = pd.read_csv('./complete.csv')
del data1['Unnamed: 0']
data.head()
del data1['X']
del data1['age']
data1.head()
data1['agePeriod']

data1.describe()

plt.style.use('seaborn-whitegrid')

data1.hist(bins=20, figsize=(60,40), color='lightblue', edgecolor = 'red')
plt.show()

def correlation_heatmap(dataframe,l,w):
    #correlations = dataframe.corr()
    correlation = dataframe.corr()
    plt.figure(figsize=(l,w))
    sns.heatmap(correlation, vmax=1, square=True,annot=True,cmap='viridis')
    plt.title('Correlation between different fearures')
    plt.show();
    
#print("After Dropping: ", cleandf)
correlation_heatmap(data1, 33,33)


corr_data = data1.corr()

print("--------------- Correlation Matrix ---------------")
mask = np.zeros_like(corr_data)
mask[np.triu_indices_from(mask)] = True
# Create the heatmap using seaborn library. 
# List if colormaps (parameter 'cmap') is available here: http://matplotlib.org/examples/color/colormaps_reference.html
sns.heatmap(corr_data, cmap='RdYlGn_r', vmax=1.0, vmin=-1 ,mask = mask,  linewidths=3,fmt='.1f')
 
# Show the plot we reorient the labels for each column and row to make them easier to read.
plt.yticks(rotation=0,fontsize=10) 
plt.xticks(rotation=45,fontsize=10) 
plt.show()

# Grid Search
param_dist = {"max_features": ['log2', 'sqrt','auto'], 
              "bootstrap": [True, False],
              "criterion": ["gini"],
              "n_estimators": [10,50,100,200]
              }
model = RandomForestClassifier()
final=GridSearchCV(model, param_dist)

final.fit(x_train,y_train)
final.best_score_

#feature importance
importances = final.best_estimator_.feature_importances_
feature_list = list(x.columns)
feature_importance= sorted(zip(importances, feature_list), reverse=True)
df = pd.DataFrame(feature_importance, columns=['importance', 'feature'])
importance= list(df['importance'])
feature= list(df['feature'])
plt.style.use('bmh')
x_values = list(range(len(feature_importance)))
plt.figure(figsize=(15,10))
plt.bar(x_values, importance, orientation = 'vertical')
plt.xticks(x_values, feature, rotation='vertical')
plt.ylabel('Importance'); plt.xlabel('Variable'); plt.title('Variable Importances');








