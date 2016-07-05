
# coding: utf-8

# In[4]:

# program to find total number/details of survived people
import pandas as pd
train_data=pd.read_csv('data1/train.csv')
# total number of passengers
total_passengers=len(train_data)
print "total number of passenngers",total_passengers
# total survived passengers
survived_passengrers_df=train_data[train_data['Survived']==1]
survived_passengrers_df[['PassengerId','Name']].to_csv('data1/Survived_passengers.csv')
survived_passengrers=survived_passengrers_df.count()['Survived']
print "count_survived_passengrers: ",survived_passengrers


# In[ ]:



