#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
A dataset collected in a cosmetics shop showing details of customers and whether or not they responded to a 
special offer to buy a new lip-stick is shown in table below. Use this dataset to build a decision tree, with 
Buys as the target variable, to help in buying lip-sticks in the future. Find the root node of decision tree. 
According to the decision tree you have made from previous training data set, 
what is the decision for the test data: [Age < 21, Income = Low, Gender = Female, Marital Status = Married]?
'''


# In[3]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
from IPython.display import Image
import pydotplus


# In[18]:


data = pd.read_csv("DecisionTree.csv")
data


# In[20]:


cleanup_nums = {
    "Age": {
        "<21": 0,
        "21-35": 1,
        ">35": 2
    },
    "Income":{
        "Low": 0,
        "Medium": 1,
        "High": 2
    },
    "Gender":{
        "Male": 0,
        "Female": 1
    },
    "Marital Status":{
        "Single": 0,
        "Married": 1
    },
    "Buys":{
        "Yes": 1,
        "No": 0
    }
}
data.replace(cleanup_nums, inplace=True)


# In[43]:


X = data[['Age', 'Income', 'Gender', 'Marital Status']]
Y = data[['Buys']]


# In[44]:


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0)
X_train


# In[45]:


clf = DecisionTreeClassifier()
clf = clf.fit(X_train, Y_train)
Y_pred = clf.predict(X_train)


# In[46]:


print("Accuracy : ", metrics.accuracy_score(Y_train, Y_pred))


# In[47]:


dot_data = StringIO()
export_graphviz(clf, out_file = dot_data, filled=True, rounded=True, special_characters=True, feature_names = ['Age', 'Income', 'Gender', 'Marital Status'], class_names=['0', '1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('buys.png')
Image(graph.create_png())


# In[48]:


# TEST data:

#value = {"Age": "< 21", "Income" = "Low", "Gender" = "Female", "Marital Status" = "Married"}

test_age = int(input("Enter 0 for <21, 1 for 21-35, and 2 for >35: "))
test_income = int(input("Enter 0 for Low, 1 for Medium, 2 for High: "))
test_gender = int(input("Enter 0 for Male, and 1 for Female: "))
test_marital_status = int(input("Enter 0 for Single, and 1 for Married: "))

test_data = [[test_age, test_income, test_gender, test_marital_status]]

prediction = clf.predict(test_data)

if(prediction[0] == 1):
    print("The person will buy the lipstick! :)")
else:
    print("The person will likely not buy the lipstick. :(")

