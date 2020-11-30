#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:36:43 2020

@author: ruihuang
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
#x_train, x_test, y_train, y_test = train_test_split(d,y,test_size=0.2,random_state=0,stratify=y)

x_train=pd.DataFrame(x_train)
x_train.head()

#用kaggle上的code KNN
from sklearn.neighbors import KNeighborsClassifier
scoreList = []
accuracies = {}
for i in range(1,20):
    knn2 = KNeighborsClassifier(n_neighbors = i)  # n_neighbors means k
    knn2.fit(x_train, y_train)
    scoreList.append(knn2.score(x_test, y_test))
    
plt.plot(range(1,20), scoreList)
plt.xticks(np.arange(1,20,1))
plt.xlabel("K value")
plt.ylabel("Score")
plt.show()

acc = max(scoreList)*100
accuracies['KNN'] = acc
print("Maximum KNN Score is {:.2f}%".format(acc))
x_train.head()

knnbest = KNeighborsClassifier(n_neighbors = 5) 
knnbest.fit(x_train, y_train)

import matplotlib.pyplot as plt
from sklearn.model_selection import validation_curve
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
pipe_knn = make_pipeline(StandardScaler(),KNeighborsClassifier(n_neighbors=5))

param_range = range(1,16)
train_scores, test_scores = validation_curve(
                estimator=pipe_knn, 
                X=x_train, 
                y=y_train, 
                param_name='kneighborsclassifier__n_neighbors', 
                param_range=param_range,
                cv=5)

train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

plt.plot(param_range, train_mean, 
         color='blue', marker='o', 
         markersize=5, label='Training accuracy')

plt.fill_between(param_range, train_mean + train_std,
                 train_mean - train_std, alpha=0.15,
                 color='blue')

plt.plot(param_range, test_mean, 
         color='green', linestyle='--', 
         marker='s', markersize=5, 
         label='Validation accuracy')

plt.fill_between(param_range, 
                 test_mean + test_std,
                 test_mean - test_std, 
                 alpha=0.15, color='green')

plt.grid()
plt.legend(loc='lower right')
plt.xlabel('Parameter k')
plt.ylabel('Accuracy')
plt.ylim([0, 1.0])
plt.tight_layout()
plt.show()

from sklearn.metrics import confusion_matrix


pipe_knn = make_pipeline(StandardScaler(),
                         KNeighborsClassifier(n_neighbors=5))

pipe_knn.fit(x_train, y_train)

y_pred = pipe_knn.predict(x_test)
confmat = confusion_matrix(y_true=y_test, y_pred=y_pred)
print(confmat)

fig, ax = plt.subplots(figsize=(2.5, 2.5))
ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)
for i in range(confmat.shape[0]):
    for j in range(confmat.shape[1]):
        ax.text(x=j, y=i, s=confmat[i, j], va='center', ha='center')

plt.xlabel('Predicted label')
plt.ylabel('True label')

plt.tight_layout()
#plt.savefig('images/601_09.png', dpi=300)
plt.show()