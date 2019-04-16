#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
In the following diagram let blue circles indicate positive examples and orange squares indicate 
negative examples. We want to use k-NN algorithm for classifying the points. If k=3, find the class 
of the point (6,6). Extend the same example for Distance-Weighted k-NN and Locally weighted Averaging
'''


# In[18]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier


# In[19]:


dataset = pd.read_csv("kNN.csv")
dataset


# In[23]:


data = dataset[['X', 'Y']]
labels = dataset[['Class']]
data


# In[ ]:





# In[24]:


# Encode Labels 
le = LabelEncoder()
# labels = le.fit_transform(labels.values.ravel())
labels


# In[35]:


# model

model = KNeighborsClassifier(n_neighbors=3, weights='distance')
model.fit(data, labels.values.ravel())

predicted= model.predict([[4,2]]) # 0:Overcast, 2:Mild
print(predicted)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




