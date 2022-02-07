#Data Camp - Comparison using Charts
#Datacamp - Chapter3
#Histogram
import pandas as pd
import matplotlib.pyplot as plt
olympics = pd.read_csv('/home/mukul/PycharmProjects/Compare_BarChart/summer2016.csv', index_col=0)
mens_rowing = olympics[olympics['Sport'] == 'Rowing']
mens_gymnastics = olympics[olympics['Sport'] == 'Gymnastics']
fig, ax = plt.subplots()

ax.boxplot([mens_rowing['Height'], mens_gymnastics['Height']])
ax.set_xticklabels(['Rowing', 'Gymnastics'])
ax.set_ylabel('Height (cm)')


plt.show()