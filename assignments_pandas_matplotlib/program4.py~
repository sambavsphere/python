import pandas as pd
list_of_cars = []
no_of_instances = input('Enter the number of car instances:\t')
# Inputs "Make1,model1,typ1,A"
for i in range(no_of_instances):
    list1=['make','model','type','rating']
    ip = raw_input("Enter the make,model,type,rating:\t")
    lz = ip.split(',')
    dict_list = zip(list1, lz)
    d= dict(dict_list)        
    list_of_cars.append(d)
df = pd.DataFrame(list_of_cars)
rating_probs = df.groupby('rating').size().div(len(df))
type_probs= df.groupby(['type', 'rating']).size().div(len(df)).div(rating_probs, axis=0, level=1)
print type_probs
