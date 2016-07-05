import pandas as pd
import numpy as np
#Loads the energy.csv file
data = pd.read_csv('energy.csv')
#Replaces the missing values with the mean energy production for that country
data.set_index('Unnamed: 0',inplace=True)
data.replace("..",np.nan,inplace=True)
data = data.fillna(0)
for column in data.columns:
    for index in data[column].index:
        if data[column][index] == 0:
            data[column][index] = data[columns].mean()
            print data[column][index]