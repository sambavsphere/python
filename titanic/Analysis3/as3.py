
# coding: utf-8

# In[1]:

# find out male and female survived proportion
import pandas as pd
df=pd.read_csv('data3/train.csv')
# total number of passengers
total_passengers=len(df)
print "total number of passenngers",total_passengers
# male female passengers count
df_total=df.groupby('Sex').count()['PassengerId']
df_total_survived=df[df['Survived']==1].groupby('Sex').count()['PassengerId']

df=pd.DataFrame(df_total_survived/df_total,columns=["PassengerId"],index=['female','male'])
df
df=df.rename(columns={'PassengerId':"Proportion"})
df.to_csv('data3/male_female_survived_proportion.csv')


# In[ ]:



