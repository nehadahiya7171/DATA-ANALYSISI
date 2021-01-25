#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[2]:


data = pd.read_csv("C:\\Users\\Thinkpad\\Pictures\\Camera Roll\Wine_data.csv")


# In[3]:


# 1 understanding the data


# In[4]:


data.head()


# In[5]:


data.tail()


# In[7]:


data.shape


# In[8]:


data.describe()


# In[9]:


data.columns


# In[10]:


data.nunique()


# In[13]:


data['Class'].unique()


# In[14]:


# cleaning the data


# In[15]:


data.isnull().sum()


# In[16]:


wine = data.drop(['Hue','Proline'], axis=1)


# In[17]:


wine.head()


# In[18]:


#3  relationship analysis


# In[19]:


corelation = wine.corr()


# In[20]:


sns.heatmap(corelation,xticklabels=corelation.columns,yticklabels=corelation.columns,annot=True)


# In[21]:


sns.pairplot(wine)


# In[27]:


sns.relplot(x='Flavanoids',y='Color intensity',data=wine)


# In[29]:


sns.distplot(wine['Alcohol'])


# In[35]:





# In[ ]:




