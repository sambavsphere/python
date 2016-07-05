import pandas as pd
import numpy as np
#Loads the energy.csv file
data = pd.read_csv('energy.csv')
#Replaces the missing values with the mean energy production for that country
data.set_index('Unnamed: 0',inplace=True)
# find out mean of every continent
means = data.mean(axis=1) 
# replace .. with mean of the continent
for index in means.index:
    l = []
    for value in data.loc[index].values:
        if value == "..":
            l.append(means[index])
        else:
            l.append(value)
    data.loc[index]=l
# Removes the data for the aggregate values (EU27, OECD, World)
data = data.drop(['EU27total','OECDtotal','World'])
continents = []
country_cont = {'Afghanistan': 'Asia',
 'Albania': 'Europe',
 'Algeria': 'Africa',
 'Andorra': 'Europe',
 'Angola': 'Africa',
 'Antigua and Barbuda': 'North America',
 'Argentina': 'South America',
 'Armenia': 'Europe',
 'Australia': 'Oceania',
 'Austria': 'Europe',
 'Azerbaijan': 'Europe',
 'Bahamas': 'North America',
 'Bahrain': 'Asia',
 'Bangladesh': 'Asia',
 'Barbados': 'North America',
 'Belarus': 'Europe',
 'Belgium': 'Europe',
 'Belize': 'North America',
 'Benin': 'Africa',
 'Bhutan': 'Asia',
 'Bolivia': 'South America',
 'Bosnia and Herzegovina': 'Europe',
 'Botswana': 'Africa',
 'Brazil': 'South America',
 'Brunei': 'Asia',
 'Bulgaria': 'Europe',
 'Burkina': 'Africa',
 'Burma (Myanmar)': 'Asia',
 'Burundi': 'Africa',
 'Cambodia': 'Asia',
 'Cameroon': 'Africa',
 'Canada': 'North America',
 'Cape Verde': 'Africa',
 'Central African Republic': 'Africa',
 'Chad': 'Africa',
 'Chile': 'South America',
 'China': 'Asia',
 'Colombia': 'South America',
 'Comoros': 'Africa',
 'Congo': 'Africa',
 'Congo, Democratic Republic of': 'Africa',
 'Costa Rica': 'North America',
 'Croatia': 'Europe',
 'Cuba': 'North America',
 'Cyprus': 'Europe',
 'CzechRepublic': 'Europe',
 'Denmark': 'Europe',
 'Djibouti': 'Africa',
 'Dominica': 'North America',
 'Dominican Republic': 'North America',
 'East Timor': 'Asia',
 'Ecuador': 'South America',
 'Egypt': 'Africa',
 'El Salvador': 'North America',
 'Equatorial Guinea': 'Africa',
 'Eritrea': 'Africa',
 'Estonia': 'Europe',
 'Ethiopia': 'Africa',
 'Fiji': 'Oceania',
 'Finland': 'Europe',
 'France': 'Europe',
 'Gabon': 'Africa',
 'Gambia': 'Africa',
 'Georgia': 'Europe',
 'Germany': 'Europe',
 'Ghana': 'Africa',
 'Greece': 'Europe',
 'Grenada': 'North America',
 'Guatemala': 'North America',
 'Guinea': 'Africa',
 'Guinea-Bissau': 'Africa',
 'Guyana': 'South America',
 'Haiti': 'North America',
 'Honduras': 'North America',
 'Hungary': 'Europe',
 'Iceland': 'Europe',
 'India': 'Asia',
 'Indonesia': 'Asia',
 'Iran': 'Asia',
 'Iraq': 'Asia',
 'Ireland': 'Europe',
 'Israel': 'Asia',
 'Italy': 'Europe',
 'Ivory Coast': 'Africa',
 'Jamaica': 'North America',
 'Japan': 'Asia',
 'Jordan': 'Asia',
 'Kazakhstan': 'Asia',
 'Kenya': 'Africa',
 'Kiribati': 'Oceania',
 'Korea': 'Asia',
 'Kuwait': 'Asia',
 'Kyrgyzstan': 'Asia',
 'Laos': 'Asia',
 'Latvia': 'Europe',
 'Lebanon': 'Asia',
 'Lesotho': 'Africa',
 'Liberia': 'Africa',
 'Libya': 'Africa',
 'Liechtenstein': 'Europe',
 'Lithuania': 'Europe',
 'Luxembourg': 'Europe',
 'Macedonia': 'Europe',
 'Madagascar': 'Africa',
 'Malawi': 'Africa',
 'Malaysia': 'Asia',
 'Maldives': 'Asia',
 'Mali': 'Africa',
 'Malta': 'Europe',
 'Marshall Islands': 'Oceania',
 'Mauritania': 'Africa',
 'Mauritius': 'Africa',
 'Mexico': 'North America',
 'Micronesia': 'Oceania',
 'Moldova': 'Europe',
 'Monaco': 'Europe',
 'Mongolia': 'Asia',
 'Montenegro': 'Europe',
 'Morocco': 'Africa',
 'Mozambique': 'Africa',
 'Namibia': 'Africa',
 'Nauru': 'Oceania',
 'Nepal': 'Asia',
 'Netherlands': 'Europe',
 'New Zealand': 'Oceania',
 'Nicaragua': 'North America',
 'Niger': 'Africa',
 'Nigeria': 'Africa',
 'Norway': 'Europe',
 'Oman': 'Asia',
 'Pakistan': 'Asia',
 'Palau': 'Oceania',
 'Panama': 'North America',
 'Papua New Guinea': 'Oceania',
 'Paraguay': 'South America',
 'Peru': 'South America',
 'Philippines': 'Asia',
 'Poland': 'Europe',
 'Portugal': 'Europe',
 'Qatar': 'Asia',
 'Romania': 'Europe',
 'RussianFederation': 'Asia',
 'Rwanda': 'Africa',
 'Saint Kitts and Nevis': 'North America',
 'Saint Lucia': 'North America',
 'Saint Vincent and the Grenadines': 'North America',
 'Samoa': 'Oceania',
 'San Marino': 'Europe',
 'Sao Tome and Principe': 'Africa',
 'Saudi Arabia': 'Asia',
 'Senegal': 'Africa',
 'Serbia': 'Europe',
 'Seychelles': 'Africa',
 'Sierra Leone': 'Africa',
 'Singapore': 'Asia',
 'Slovakia': 'Europe',
 'Slovenia': 'Europe',
 'Solomon Islands': 'Oceania',
 'Somalia': 'Africa',
 'SouthAfrica': 'Africa',
 'South Sudan': 'Africa',
 'Spain': 'Europe',
 'Sri Lanka': 'Asia',
 'Sudan': 'Africa',
 'Suriname': 'South America',
 'Swaziland': 'Africa',
 'Sweden': 'Europe',
 'Switzerland': 'Europe',
 'Syria': 'Asia',
 'Tajikistan': 'Asia',
 'Tanzania': 'Africa',
 'Thailand': 'Asia',
 'Togo': 'Africa',
 'Tonga': 'Oceania',
 'Trinidad and Tobago': 'North America',
 'Tunisia': 'Africa',
 'Turkey': 'Asia',
 'Turkmenistan': 'Asia',
 'Tuvalu': 'Oceania',
 'Uganda': 'Africa',
 'Ukraine': 'Europe',
 'United Arab Emirates': 'Asia',
 'United Kingdom': 'Europe',
 'United States': 'North America',
 'Uruguay': 'South America',
 'Uzbekistan': 'Asia',
 'Vanuatu': 'Oceania',
 'Vatican City': 'Europe',
 'Venezuela': 'South America',
 'Vietnam': 'Asia',
 'Yemen': 'Asia',
 'Zambia': 'Africa',
'NewZealand':'Oceania',
'SlovakRepublic':'Europe',
'UnitedKingdom':'Europe',
'UnitedStates':' North America',
 'Zimbabwe': 'Africa'}
for index in data.index:
    continents.append(country_cont[index])
data['continent']=continents
contenent_group = data.groupby('continent')
num_countries = contenent_group.count()
mean = contenent_group.mean()
small_production = {}
large_production = {}
avg_production = {}
for cont in num_countries.index:
    if data[data['continent']==cont].mean()['1990'] < (data.mean()-data.std())['1990']:
        small_production.update({cont:1})
    else:
        small_production.update({cont:0})
for cont in num_countries.index:
    if data[data['continent']==cont].mean()['1990'] > (data.mean()+data.std())['1990']:
        large_production.update({cont:1})
    else:
        large_production.update({cont:0})
for cont in num_countries.index:
    if (data[data['continent']==cont].mean()['1990'] > (data.mean()-data.std())['1990']) & (data[data['continent']==cont].mean()['1990'] < (data.mean()+data.std())['1990']):
        avg_production.update({cont:1})
    else:
        avg_production.update({cont:0})
dataframe = pd.DataFrame([dict(num_countries['1990']),dict(mean['1990']),small_production,large_production,avg_production]
                     ).T
dataframe.columns = ['num_countries','mean','small_production','large_production','avg_production']
print dataframe
