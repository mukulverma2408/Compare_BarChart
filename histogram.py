#Data Camp - Comparison using Charts
#Datacamp - Chapter3
#Histogram
import pandas as pd
import matplotlib.pyplot as plt
olympics = pd.read_csv('/home/mukul/PycharmProjects/Compare_BarChart/summer2016.csv', index_col=0)
mens_rowing = olympics[olympics['Sport'] == 'Rowing']
mens_gymnastics = olympics[olympics['Sport'] == 'Gymnastics']
print(mens_rowing.info())
print(mens_gymnastics.info())
fig, ax = plt.subplots()

ax.bar("Rowing", mens_rowing['Height'].mean(), yerr=mens_rowing['Height'].std())
ax.bar("Gymnastics", mens_gymnastics['Height'].mean(), yerr=mens_gymnastics['Height'].std())
ax.set_ylabel("Height (cm)")

#ax.hist(mens_rowing['Weight'], label='Rowing', histtype='step', bins=5)
#ax.hist(mens_gymnastics['Weight'], label='Gymnastics', histtype='step', bins=5)
#ax.set_xlabel('Weight (kg)')
#ax.set_ylabel('# of observations')
#ax.legend()
plt.show()