import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('ASML.AS.csv')

df['Date'] = pd.to_datetime(df['Date'])
df = df.rename(columns={'Close':'Closing price (€)'})

# splot_lin = sns.regplot(x='Date', y='Close', data=df, fit_reg=False)
plt.figure()
splot1 = sns.regplot(x='Date', y='Closing price (€)', data=df, fit_reg=False, scatter_kws={'s':5})
plt.figure()
splot = sns.regplot(x='Date', y='Closing price (€)', data=df, fit_reg=False, scatter_kws={'s':5})
splot.set(yscale="log")
splot.set(ylim=(0, 1500))
ylab = splot.get_yticks()
# ylab = splot.get_yticklabels()
labels = ['%.0f' % float(t) for t in ylab]
splot.set_yticklabels(labels)
# splot.set_yticks(labels)
# splot.set_y

##
# splot.yticks(splot.get_yticks(), splot.get_yticks() * 10)

t = splot.get_yticks()

[print(x) for x in t]