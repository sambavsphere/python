
# coding: utf-8

# In[7]:

import pandas as pd
import numpy as np
import sys
data=pd.read_csv('data.csv')
l=['A','C','G','T']
sequence_str=raw_input("Enter sequesnce:")
for i in sequence_str:
    if i not in l:
        print ("Sequence letters should contains (ACGT)")
        sys.exit(0)
sequence_list=list(sequence_str)
stages_str=raw_input("Enter Stages:")
if len(stages_str)>3:
    print ("stages should not greaterthan 3")
    sys.exit(0)
stages_list=list(stages_str)
loopin_values=[]
for i in stages_list:
    s=float(raw_input("Looping value for %s:"%i))
    loopin_values.append(s)
loopin_values=pd.DataFrame(data=loopin_values,index=stages_list)
stage_transformation_values=[]
key="start->%s"%stages_list[0]
s1=float(raw_input("Stage transformation value:%s:"%key ))
stage_transformation_values.append(s1)
j=1
for i in stages_list:
     if i==stages_list[-1]:
        break
     key="%s->%s"%(i,stages_list[j])
     s2=float(raw_input("Stage transformation value:%s:"%key))
     stage_transformation_values.append(s2)
     j=j+1
key="%s->%s"%(stages_list[-1],"End")
s3=float(raw_input("Stage transformation value:%s:"%key))
stage_transformation_values.append(s3)
result_df=pd.DataFrame(data=np.random.randn(len(stages_list),len(sequence_list)),index=stages_list)
data.index=stages_list
k=0
stagetransfromation=1
for i,stage in zip(result_df.index,stage_transformation_values):
    looping=1
    computed_value=1
    for p in range(k):
        result_df[result_df.columns[p]][i]=0
    columns=result_df.columns[k:]
    previous_column=result_df.columns[k-1]
    for j in columns:
        computed_value=computed_value*float(data[sequence_list[j]][i])*float(looping)*float(stagetransfromation)
        previouscolumnpreviousindexvalue=0
        if k>0:
            previouscolumnpreviousindexvalue=result_df[previous_column][previous_stage]
        exact_value=max([computed_value,previouscolumnpreviousindexvalue])
        looping=loopin_values[0][i]
        result_df[j][i]=exact_value
        if k>0:
            previous_column=j
    previous_stage=i
    k=k+1
    stagetransfromation=stage
columns_map={}
for i,j in zip(result_df.columns,sequence_list):
    columns_map.update({i:j})
result_df=result_df.rename(columns_map)
print result_df

