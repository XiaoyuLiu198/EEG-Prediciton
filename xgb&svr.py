#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import warnings
import seaborn as sns
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')
data_alpha=pd.read_csv("E://605_proj/alpha.csv")
data_beta=pd.read_csv("E://605_proj/beta.csv")
data_sigma=pd.read_csv("E://605_proj/sigma.csv")
data_sita=pd.read_csv("E://605_proj/sita.csv")
data_entropy=pd.read_csv("E://605_proj/entropy.csv")


# In[2]:


from matplotlib.ticker import MultipleLocator,FormatStrFormatter
colormap = plt.cm.viridis
plt.figure(figsize=(12,12))
plt.title('Pearson Correlation of Features', y=1.05, size=15)
sns.heatmap(data_alpha.astype(float).corr(),linewidths=0.1,vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)


# In[3]:


colormap = plt.cm.viridis
plt.figure(figsize=(12,12))
plt.title('Pearson Correlation of Features', y=1.05, size=15)
sns.heatmap(data_beta.astype(float).corr(),linewidths=0.1,vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)


# In[4]:


colormap = plt.cm.viridis
plt.figure(figsize=(12,12))
plt.title('Pearson Correlation of Features', y=1.05, size=15)
sns.heatmap(data_sigma.astype(float).corr(),linewidths=0.1,vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)


# In[7]:


colormap = plt.cm.viridis
plt.figure(figsize=(12,12))
plt.title('Pearson Correlation of Features', y=1.05, size=15)
sns.heatmap(data_sita.astype(float).corr(),linewidths=0.1,vmax=1.0, square=True, cmap=colormap, linecolor='white')


# In[6]:


colormap = plt.cm.viridis
plt.figure(figsize=(12,12))
plt.title('Pearson Correlation of Features', y=1.05, size=15)
sns.heatmap(data_entropy.astype(float).corr(),linewidths=0.1,vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)


# In[9]:


x=data_sita["age"]
y=data_sita["EEG.EKG1.REF"]
plt.scatter(x, y)
plt.title("Age-Channel EEG.EKG1.REF")
plt.xlabel("Age")
plt.ylabel("EEG.EKG1.REF")


# In[10]:


x=data_sita["age"]
y=data_sita["EEG.P4.REF"]
plt.scatter(x, y)
plt.title("Age-Channel EEG.P4.REF")
plt.xlabel("Age")
plt.ylabel("EEG.P4.REF")


# In[11]:


x=data_sita["age"]
y=data_sita["EEG.O1.REF"]
plt.scatter(x, y)
plt.title("Age-Channel EEG.O1.REF")
plt.xlabel("Age")
plt.ylabel("EEG.O1.REF")


# In[13]:


data=data_sita.copy(deep=True)


# In[46]:


data=data_alpha.copy(deep=True)


# In[47]:


from sklearn.decomposition import PCA
#explained_ratio=[]
#for i in range(5,len(data)):
pca = PCA(n_components=23)
pca.fit(data.iloc[:,1:25])
print(pca.explained_variance_ratio_)


# In[24]:


data.iloc[:,1:25]


# In[49]:


data1=pca.transform(data.iloc[:,1:25])


# In[50]:


from xgboost.sklearn import XGBRegressor
from sklearn.model_selection import GridSearchCV
warnings.filterwarnings('ignore')
xgb1 = XGBRegressor()
parameters = {'objective':['reg:squarederror'],
              'learning_rate': [.003,.006,.01,.015,.02,.03, 0.05, .07], #so called `eta` value
              'max_depth': [5, 6, 7],
              'min_child_weight': [2,3,4,5],
              'n_estimators': [500]}

xgb_grid = GridSearchCV(xgb1,
                        parameters,
                        cv = 2,
                        n_jobs=3,
                        verbose=True)

xgb_grid.fit(data1,data["age"])

print(xgb_grid.best_score_)
print(xgb_grid.best_params_)


# In[ ]:


pd.DataFrame.from_dict(xgb_grid.cv_results_)


# In[ ]:


##SVR
from sklearn.svm import SVR
param = {'kernel' : ('poly', 'rbf'),'C' : [1,5,10],'degree' : [3,8],'coef0' : [0.01,10,0.5],'gamma' : ('auto','scale')}

modelsvr = SVR()

svrgrid = GridSearchCV(modelsvr,param,cv=3)

svrgrid.fit(data1,data["age"])
print(svrgrid.best_score_)
print(svrgrid.best_params_)


# In[ ]:




