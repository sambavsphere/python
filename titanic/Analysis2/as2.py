
# coding: utf-8

# In[1]:

# program to find out proportion of survived people
import pandas as pd
data=pd.read_csv('data2/train.csv')
# total number of passengers
total_passengers=len(data)
print "total number of passenngers",total_passengers
# total survived passengers
survived_passengrers_df=data[data['Survived']==1]
# proportion_survivors
survived_passengrers=survived_passengrers_df.count()['Survived']
proportion_survivors=survived_passengrers/float(total_passengers)
f=open('data2/total_survived_proportion.csv','w')
f.write("Total proportion:"+str(proportion_survivors))
f.close()


# In[ ]:



