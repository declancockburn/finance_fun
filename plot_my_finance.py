import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Todo: tidy up a little more, labels, marker widths etc.
#  Put dates at an angle to fit
#  Add horizontal bars or numbers, or something to designate events/decisions.
#  Decide what decision points, and what to write (check notes!)

# Note: What decision points discription? Move-windfall, car-import, market stop + bad decisions, big gap why.
#  Check notes in excel.


# Set some plot constants:
cm = 1/2.54  # centimeters in inches
px = 1/plt.rcParams['figure.dpi']

# set seaborn style
# sns.set_theme()
plt.style.use('seaborn')
df_og = pd.read_csv('finance - Overall.csv')
df = df_og.copy()
df['date'] = pd.to_datetime(df['date'], format="%d/%m/%Y")
# df.plot('date', 'total-est-NW')

last_row = df['date'].dropna().index[-1]
df = df.iloc[:last_row+1]
items = ['date', 'Eq+', 'US BA', 'TW BA', 'Dutch BA', 'Irish BA', 'car_cost', 'degiro', 'Crypto', 'P2P',
         'Property Value Owned', 'Owe ASML', 'Assets (no car/hs)', 'total-est-NW']
df = df[items]
df = df.fillna(0)

bank_acc = ['US BA', 'TW BA', 'Dutch BA', 'Irish BA', 'Owe ASML']
df['Bank'] = df.loc[:, bank_acc].sum(axis=1)
df = df.drop(columns=bank_acc)

equity = ['Eq+', 'degiro']
df['Stocks'] = df.loc[:, equity].sum(axis=1)
df = df.drop(columns=equity)

df = df.rename(columns={'car_cost': 'Car import', 'Property Value Owned': 'Property',
                        'date': 'Date', 'total-est-NW': 'Total-NW'})

# euro sign € \u20ac

df_total = df[['Date', 'Total-NW']]
df_area = df[['Date', 'Property', 'Crypto', 'Stocks', 'Bank', 'Car import', 'P2P']]

df_perc = df_area.drop(columns = ['Date'])
df_perc = df_perc.divide(df_perc.sum(axis=1), axis=0)*100
df_perc = pd.concat([df_area['Date'], df_perc], axis=1)
df_perc_total = df_total.copy()
df_perc_total['Total-NW'] = 100

figsize = (25*cm, 14*cm)

fig, ax = plt.subplots(figsize=figsize)
df_area.plot.area(x='Date', ax=ax, linewidth=0)
df_total.plot.scatter(x='Date', y='Total-NW', ax=ax)


fig2, ax2 = plt.subplots(figsize=figsize)
df_perc.plot.area(x='Date', ax=ax2, linewidth=0)
df_perc_total.plot.scatter(x='Date', y='Total-NW', ax=ax2)
plt.title('100% stacked area chart')
plt.ylabel('% of total NW')



fig3, ax3 = plt.subplots(2, 3, sharex=True, sharey=True, figsize=figsize)
df_area2 = df_area.copy()
df_area2 = df_area2.replace({'0':np.nan, 0:np.nan})
ylims = (0, df_area2.iloc[:,1:].max().max()*1.05)
colors = [x.get_c() for x in ax.get_lines()]
for i in range(2):
    for j in range(3):
        num = j+i*3
        df_area2.plot.area(x='Date', y=df_area2.columns[num+1], ax=ax3[i,j], linewidth=0, color=f'{colors[num]}')
        df_area2.plot.scatter(x='Date', y=df_area2.columns[num+1], ax=ax3[i,j], marker='|', color='black', linewidth=1)
        ax3[i,j].set_ylim(ylims)



# df_perc.plot.area(x='Date', ax=ax2, linewidth=0)
# df_perc_total.plot.scatter(x='Date', y='Total-NW', ax=ax2)
# plt.title('100% stacked area chart')
# plt.ylabel('% of total NW')


##

# ax.stackplot(df['date'], df[items],
#              labels=items)

# df[items].values

# # data from United Nations World Population Prospects (Revision 2019)
# # https://population.un.org/wpp/, license: CC BY 3.0 IGO
# year = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2018]
# population_by_continent = {
#     'africa': [228, 284, 365, 477, 631, 814, 1044, 1275],
#     'americas': [340, 425, 519, 619, 727, 840, 943, 1006],
#     'asia': [1394, 1686, 2120, 2625, 3202, 3714, 4169, 4560],
#     'europe': [220, 253, 276, 295, 310, 303, 294, 293],
#     'oceania': [12, 15, 19, 22, 26, 31, 36, 39],
# }
# population_by_continent.values()
#
# df[items]
#
# [print(df[col].dtype) for col in df[items]]
#
#
# fig, ax = plt.subplots()
# ax.stackplot(year, population_by_continent.values(),
#              labels=population_by_continent.keys())
# ax.legend(loc='upper left')
# ax.set_title('World population')
# ax.set_xlabel('Year')
# ax.set_ylabel('Number of people (millions)')

plt.show()