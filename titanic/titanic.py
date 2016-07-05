
# coding: utf-8

# In[2]:

import pandas as pd
import matplotlib as plt


# In[3]:

# getting traiuning data into python variable
train_data=pd.read_csv('data/train.csv')


# In[4]:

# total number of passengers
total_passengers=len(train_data)
print "total number of passenngers",total_passengers


# In[5]:

# total survived passengers
survived_passengrers_df=train_data[train_data['Survived']==1]
survived_passengrers_df[['PassengerId','Name']].to_csv('data/Survived_passengers.csv')
survived_passengrers=survived_passengrers_df.count()['Survived']
survived_passengrers


# In[6]:

# proportion_survivors
proportion_survivors=survived_passengrers/float(total_passengers)
proportion_survivors


# In[7]:

# find out number of women and men count
total_male_female=train_data.Sex.value_counts()
total_male_female


# In[8]:

# Number of survied passengers women and men count
survived_passengrers_female=train_data[(train_data['Survived']==1)                                       & (train_data['Sex']=='female')]
survived_passengrers_male=train_data[(train_data['Survived']==1)                                       & (train_data['Sex']=='male')]
survived_passengrers_female[['PassengerId','Name']].to_csv('data/survived_passengrers_female.csv')
survived_passengrers=train_data[train_data['Survived']==1].Sex.value_counts()
survived_passengrers


# In[9]:

# men_proportion_survivors
men_proportion_survivors=total_male_female['male']/float(total_passengers)
men_proportion_survivors


# In[10]:

# women_proportion_survivors
women_proportion_survivors=total_male_female['female']/float(total_passengers)
women_proportion_survivors


# In[11]:

# Maximum fare?
max_fare=train_data['Fare'].max()
max_fare


# In[12]:

# Min fare?
min_fare=train_data['Fare'].min()
min_fare


# In[13]:

# passengerid with fare=0
fare_0=train_data[train_data['Fare']==min_fare][['PassengerId','Name','Fare']]
fare_0.to_csv('data/fare_0.csv')
fare_0


# In[14]:

# count of minfare passenges
fare_0.count()['PassengerId']


# In[15]:

# passengerid with fare>400
faregt400=train_data[train_data['Fare']>400][['PassengerId','Name','Fare']]
faregt400.to_csv('data/faregt400.csv')
faregt400


# In[16]:

# passengerid with fare>400 count
faregt400.count()['PassengerId']


# In[17]:


train_data.columns


# In[22]:

# class wise classification
class_classification=train_data.Pclass.value_counts()
class_classification


# In[32]:

# 3rd class survived people
survived_3rdclass=train_data[(train_data['Pclass']==3) & (train_data['Survived']==1)]
survived_3rdclass.to_csv('survived_3rdclass.cv')
survived_3rdclass.count()['PassengerId']


# In[33]:

# 2nd class survived people
survived_2ndclass=train_data[(train_data['Pclass']==2) & (train_data['Survived']==1)]
survived_2ndclass.to_csv('survived_2ndclass.cv')
survived_2ndclass.count()['PassengerId']


# In[34]:

# 1st class survived people
survived_1stclass=train_data[(train_data['Pclass']==1) & (train_data['Survived']==1)]
survived_1stclass.to_csv('survived_1stclass.cv')
survived_1stclass.count()['PassengerId']


# In[50]:

#class_wise_proportion
df_t=train_data.groupby('Pclass').count()['PassengerId']
df_s=train_data[train_data['Survived']==1].groupby('Pclass').count()['PassengerId']

pd.DataFrame(df_s/df_t,columns=["PassengerId"],index=[1,2,3])


# In[ ]:



