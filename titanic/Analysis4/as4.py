
# coding: utf-8

# In[3]:

import pandas as pd
titanic_data=pd.read_csv('data4/train.csv')
# total number of passengers
total_passengers=len(titanic_data)
print "total number of passenngers",total_passengers
#class_wise_proportion
df_t=titanic_data.groupby('Pclass').count()['PassengerId']
df_s=titanic_data[titanic_data['Survived']==1].groupby('Pclass').count()['PassengerId']
df=pd.DataFrame(df_s/df_t,columns=["PassengerId"],index=[1,2,3])
df=df.rename(columns={"PassengerId":"proportion"})
df.to_csv('data4/class_wise_proportion.csv')


# In[ ]:



