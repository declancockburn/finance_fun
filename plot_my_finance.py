import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# set seaborn style
# sns.set_theme()
plt.style.use('seaborn')
df_og = pd.read_csv('finance.csv')
df = df_og.copy()
df['date'] = pd.to_datetime(df['date'], format="%d/%m/%Y")
# df.plot('date', 'total-est-NW')

last_row = df['date'].dropna().index[-1]
df = df.iloc[:last_row+1]
items = ['date', 'Eq+', 'US BA', 'TW BA', 'Dutch BA', 'Irish BA', 'car_cost', 'degiro', 'P2P', 'Property Value Owned', 'Owe ASML']
df = df[items]
df = df.fillna(0)

bank_acc = ['US BA', 'TW BA', 'Dutch BA', 'Irish BA', 'Owe ASML']
df['Bank'] = df.loc[:, bank_acc].sum(axis=1)
df = df.drop(columns=bank_acc)

equity = ['Eq+', 'degiro']
df['Equity'] = df.loc[:, equity].sum(axis=1)
df = df.drop(columns=equity)

df = df.rename(columns={'car_cost': 'Mustang', 'Property Value Owned': 'Property'})

df = df[['date', 'Property', 'Equity', 'Bank', 'Mustang', 'P2P']]

# fig, ax = plt.subplots()
df.plot.area(x='date')



##

ax.stackplot(df['date'], df[items],
             labels=items)

# df[items].values

# data from United Nations World Population Prospects (Revision 2019)
# https://population.un.org/wpp/, license: CC BY 3.0 IGO
year = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2018]
population_by_continent = {
    'africa': [228, 284, 365, 477, 631, 814, 1044, 1275],
    'americas': [340, 425, 519, 619, 727, 840, 943, 1006],
    'asia': [1394, 1686, 2120, 2625, 3202, 3714, 4169, 4560],
    'europe': [220, 253, 276, 295, 310, 303, 294, 293],
    'oceania': [12, 15, 19, 22, 26, 31, 36, 39],
}
population_by_continent.values()

df[items]

[print(df[col].dtype) for col in df[items]]


fig, ax = plt.subplots()
ax.stackplot(year, population_by_continent.values(),
             labels=population_by_continent.keys())
ax.legend(loc='upper left')
ax.set_title('World population')
ax.set_xlabel('Year')
ax.set_ylabel('Number of people (millions)')

plt.show()