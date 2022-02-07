#Data Camp - Comparison using Charts
#Datacamp - Chapter3
#Scatter Plot
import pandas as pd
import matplotlib.pyplot as plt
climate_change = pd.read_csv("/home/mukul/PycharmProjects/Compare_BarChart/climate_change.csv", index_col=0)
#print(climate_change.head())
fig, ax = plt.subplots()
climate_change.index = pd.to_datetime(climate_change.index)
ax.scatter(climate_change['co2'], climate_change['relative_temp'], c=climate_change.index)
ax.set_xlabel('CO2 (ppm)')
ax.set_ylabel('Relative temperature (C)')
plt.show()