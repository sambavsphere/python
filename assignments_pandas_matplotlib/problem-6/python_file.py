import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def piechart_plot(df):
    hhl_lan = ['English only', 'Spanish', 'Other Indo-European languages', 'Asian and Pacific Island languages','Other language']
    hhl_lan_count = df['HHL'].value_counts().to_dict()
    for i in hhl_lan_count:
        if i == 1.0:
            hhl_lan_count['English only'] = hhl_lan_count.pop(i)
        elif i == 2.0:
            hhl_lan_count['Spanish'] = hhl_lan_count.pop(i)
        elif i == 3.0:
            hhl_lan_count['Other Indo-European languages'] = hhl_lan_count.pop(i)
        elif i == 4.0:
            hhl_lan_count['Asian and Pacific Island languages'] = hhl_lan_count.pop(i)
        elif i == 5.0:
            hhl_lan_count['Other language'] = hhl_lan_count.pop(i)

        # Pie Chart
    labels = hhl_lan_count.keys()
    sizes = hhl_lan_count.values()
    colors = ['#cc0099', 'blue', '#00bfff', 'green','red']
    patches, texts = plt.pie(sizes, colors=colors, startangle=240)
    plt.legend(patches, labels, loc=2).draggable()
    plt.axis('equal')
    plt.title('Household Languages')
    plt.tight_layout()
    #plt.show()
plt.subplot(2,2,1)
df = pd.read_csv('ss13hil.csv')
piechart_plot(df)
plt.subplot(2,2,2)

mu = 100  # mean of distribution
sigma = 15  # standard deviation of distribution
x = df['HINCP'].dropna().values.tolist()
num_bins = 60

# the histogram of the data
n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='green', alpha=0.5)
y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'b--')
plt.xlabel('Household Income($) - Log scaled')
plt.ylabel('Density')
plt.title('Distribution of Household Income')

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.grid(True)

plt.subplot(2,2,3)
#Bar Chart 
bar_gropu = df.groupby('VEH').sum()['WGTP']
x=bar_gropu.index.tolist()
y=bar_gropu.values.tolist()
plt.bar(x,y,label='Bar1',color='r')
plt.xlabel('# of Vehicles')
plt.ylabel('Thousands of house holds')
plt.title('Vehicla Available in Households')

plt.subplot(2,2,4)
# Scatter Plot
xyc = range(100)
cm = plt.cm.get_cmap('Accent')
sc = plt.scatter(xyc, xyc, c=xyc, s=35, vmin=0, vmax=20, cmap=cm)
plt.colorbar(sc)
plt.xlim(0, 20)
plt.ylim(0, 20)

plt.show()



