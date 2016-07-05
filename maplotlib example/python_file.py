import matplotlib.pyplot as plt

plt.rcdefaults()

import numpy as np

import matplotlib.pyplot as plt

import pandas as pd

data=pd.read_csv('Infectious_Disease_Cases_by_County__Year__and_Sex__2001-2014.csv')

data_g=data.groupby(['Year','Sex']).sum()['Count']

data_g.plot(kind="bar")

plt.show()

data_g.plot(kind="hist")

plt.show()

data_g.plot(kind="area")

plt.show()

data_g.plot(kind="pie",figsize=(6, 6))

plt.show()

data_g.plot(kind="line")

plt.show()

data_g_d=data.groupby(['Year','Disease','Sex']).sum().sort_index(by="Count",ascending=False)['Count'][2001].head(10)

data_g_d.plot(kind="bar")

plt.show()

data_g_d.plot(kind="hist")

plt.show()

data_g_d.plot(kind="area")

plt.show()

data_g_d.plot(kind="pie",figsize=(6, 6))

plt.show()

data_g_d.plot(kind="line")

plt.show()