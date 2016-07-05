import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import re
fig=plt.figure() #Plots in matplotlib reside within a figure object, use plt.figure to create new figure
df=pd.read_csv('imdb_ratings.csv',sep=";")
df.columns=[i.strip(',') for i in df.columns]
df['Title']=[str(i).strip(',')  for i in df['Title']]
df['Year']=df['Title'].apply(lambda x: re.findall("\(\d{4}\)",x)[0][1:5] if re.findall("\(\d{4}\)",x) else '')
# table for the movies count year wise
df_year_group_line=df.groupby('Year').count().cumsum()
print df_year_group_line
# line graph for the movies count year wise
df_year_group_line.plot(y="Title")
plt.show()
# bar graph for the movies count year wise
df_year_group_line.plot(y="Title",kind="bar")
plt.show()
# table representaion for the max voted movies in the year wise
df_year_group_max=df.groupby('Year').max()
print df_year_group_max.ix[1:]
# line graph for the max voted movies in the year
df_year_group_v_bar=df.groupby('Year').max()
df_year_group.plot(y="Votes")
plt.show()
# bar graph for the max voted movies in the year
df_year_group_v_bar=df.groupby('Year').max()
df_year_group.plot(y="Votes",kind="bar")
plt.show()
# Table representation for the max ranked movies in the year
df_year_group_r_bar=df.groupby(['Year'], sort=False)['Rank','Title'].max()
print df_year_group_r_bar
# line graph for the max ranked movies in the year
df_year_group_r_bar.plot(y="Rank")
plt.show()
# bar graph for the max ranked movies in the year
df_year_group_r_bar.plot(y="Rank",kind="bar")
plt.show()
# Heighest rank movies in the total years
print df[df['Rank']==max(df['Rank'])]
# Heighest voted movies in the total years
print df[df['Votes']==max(df['Votes'])]