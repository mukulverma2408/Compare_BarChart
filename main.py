#Data Camp - Comparison using Charts
#Datacamp - Chapter3
#Medals Bar Comparison
import pandas as pd
import matplotlib.pyplot as plt
medals = pd.read_csv('/home/mukul/PycharmProjects/Compare_BarChart/medals_by_country_2016.csv', index_col=0)
fig, ax = plt.subplots()
ax.bar(medals.index, medals['Gold'], label='Gold')
ax.bar(medals.index, medals['Silver'], bottom=medals['Gold'], label='Silver')
ax.bar(medals.index, medals['Bronze'], bottom=medals['Gold'] + medals['Silver'], label='Bronze')
ax.set_xticklabels(medals.index, rotation=90)
ax.set_ylabel('Numbers of Medals')
ax.legend()
plt.show()

