#!/usr/bin/env python
# coding: utf-8

# In[6]:


'''
We have given a collection of 8 points. P1=[0.1,0.6] P2=[0.15,0.71] 
P3=[0.08,0.9] P4=[0.16, 0.85] P5=[0.2,0.3] P6=[0.25,0.5] P7=[0.24,0.1] 
P8=[0.3,0.2]. Perform the k-mean clustering with initial centroids as m1=P1 =Cluster#1=C1 and m2=P8=cluster#2=C2. Answer the following
1] Which cluster does P6 belongs to?
2] What is the population of cluster around m2? 
3] What is updated value of m1 and m2?
'''


# In[7]:


from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


# In[35]:


dataset = pd.read_csv('kMeansClustering.csv')
dataset


# In[42]:


centroids = np.array([[0.1, 0.6], [0.3, 0.2]])
kmeans = KMeans(n_clusters=2, init=centroids)
kmeans = kmeans.fit(dataset)


# In[55]:


print("Labels\n",kmeans.labels_)


# In[56]:


print("Updated Centroids\n",kmeans.cluster_centers_)


# In[57]:


plt.scatter(dataset['X'], dataset['Y'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', s=50)
plt.show()


# In[37]:


val = kmeans.predict([[0.25,0.5]])
print(val)


# In[46]:


count = 0
for label in kmeans.labels_:
    if label == 1:
        count += 1
count


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




