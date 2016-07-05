
# coding: utf-8

# In[1]:

# program to find out total passendgers and survived passengers and proportion class wise
import pandas as pd
data_titanic=pd.read_csv('data5/train.csv')
# total number of passengers
total_passengers=len(data_titanic)
print "total number of passenngers",total_passengers
df_count_clss=data_titanic.groupby('Pclass').count()['PassengerId']
df_count_clss_survived=data_titanic[data_titanic['Survived']==1].groupby('Pclass').count()['PassengerId']
df=pd.DataFrame({})
df['total']=df_count_clss.values
df['survived']=df_count_clss_survived.values
df['proportion']=(df_count_clss_survived/df_count_clss).values
df.to_csv('data5/proport_class.csv')


# In[ ]:



