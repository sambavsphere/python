# importing modules
import sys
l=['A','C','G','T'] # minimal sequence list check whether user enterd the seaquence belongs to these letter or no
sequence_str=raw_input("Enter sequesnce:") # getting the sequence from the user
sequence_str=sequence_str.upper() # making the sequence into uppercase
for i in sequence_str:
    '''
    does the sequence contains any other letters
    '''
    if i not in l:
        print ("Sequence letters shouldnot contains other than(ACGT)")
        sys.exit(0)

sequence_list=list(sequence_str) # convert sequence string to sequence list
stages_str=raw_input("Enter Stages:") # getting the stages here from the user
stages_list=list(stages_str) # convert stages string to stages list
loopin_values={}
for i in stages_list:
    '''
    loop throught stages asking for looping value
    '''
    s=float(raw_input("Looping value for %s:"%i)) # get looping value from the user
    loopin_values.update({i:s}) # appending looping value to the list
stage_transformation_values=[]

# to get stage transformation value from the user

key="start->%s"%stages_list[0]
s1=float(raw_input("Stage transformation value:%s:"%key ))
stage_transformation_values.append(s1)
j=1
for i in stages_list:
     '''
     Looping through the stages to get 
     '''
     if i==stages_list[-1]:
        break
     key="%s->%s"%(i,stages_list[j])
     s2=float(raw_input("Stage transformation value:%s:"%key))
     stage_transformation_values.append(s2)
     j=j+1
key="%s->%s"%(stages_list[-1],"End")
s3=float(raw_input("Stage transformation value:%s:"%key))
# to get stage transformation value from the user

# getting Minimal Sequence values from the user at every stage
data={}
stage_transformation_values.append(s3)
for j in stages_list:
    '''
    Looping through the stages
    '''
    sequenc_dict={}
    for i in l:
        '''
        Looping throught minimal sequence to get the values at every stage
        '''

        d1=float(raw_input("Enter "+i+" value at stage:"+j+":"))
        sequenc_dict.update({i:d1})
    data.update({j:sequenc_dict})
result_df={}  
k=0
for i in stages_list:
    result_df.update({i:{}})
stagetransfromation=1
for i,stage in zip(stages_list,stage_transformation_values):
    looping=1
    computed_value=1
    stage_dict={}
    for p in range(k):
        stage_dict.update({k:0})
        #result_df[result_df.columns[p]][i]=0
    columns=range(k,len(sequence_list))
    previous_column=k-1
    for j in columns:
        computed_value=computed_value*float(data[i][sequence_list[j]])*float(looping)*float(stagetransfromation)
        previouscolumnpreviousindexvalue=0
        if k>0:
            previouscolumnpreviousindexvalue=result_df[previous_stage][previous_column]
        exact_value=max([computed_value,previouscolumnpreviousindexvalue])
        looping=loopin_values[i]
        result_df[i][j]=exact_value
        if k>0:
            previous_column=j
    previous_stage=i
    k=k+1
    stagetransfromation=stage
res1="\t"
for k,k2 in zip(sequence_list,range(len(sequence_list))):
    res1=res1+k2*"   "+str(k)
print res1
for i in stages_list:
    res=str(i)+"\t"
    for j in range(len(sequence_list)):
        res=res+" "+str(result_df[i].get(j,0.0))
    print res




