#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''The following table shows the results of a recently conducted 
study on the correlation of the number of hours spent driving with 
the risk of developing acute backache. Find the equation of the 
best fit line for this data.'''


# In[4]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


# In[5]:


dataset = pd.read_csv("LinearRegression.csv")


# In[6]:


dataset


# In[7]:


X = dataset[['Hours']]
Y = dataset[['Risk']]


# In[8]:


mLinearRegression = LinearRegression()
mLinearRegression.fit(X, Y)


# In[9]:


b0 = mLinearRegression.intercept_
b1 = mLinearRegression.coef_


# In[13]:


print("Equation of best fit y = ", b0[0] , " + " , b1[0][0] , "x")


# In[22]:


x_input = input("Enter the number of hours you drive to find out how much risk you are taking: ")
x_input = int(x_input)
y_pred = mLinearRegression.predict(np.array([[x_input]]))
print("You are taking a risk of ", y_pred[0][0], "%")


# In[23]:


## Accuracy

accuracy = mLinearRegression.score(X, Y) * 100
print("Accuracy of the Linear Regression model is : ", accuracy)


# In[24]:


predictions = mLinearRegression.predict(X)
plt.scatter(X, Y)
plt.plot(X, predictions, color='blue', linewidth=1)
plt.show()


# In[ ]:




