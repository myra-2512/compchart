import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data=pd.read_csv('FuelConsumption.csv')
print(data.head())
print(data.isnull().any())

df_grouped = data.groupby('VEHICLECLASS')[[

'FUELCONSUMPTION_CITY',

'FUELCONSUMPTION_HWY',

'FUELCONSUMPTION_COMB'

]].mean().reset_index()
print(df_grouped.head())

x=np.arange(0,len(df_grouped.index))

plt.bar(x, df_grouped['FUELCONSUMPTION_HWY'], color='#8390FA')
plt.show()


plt.bar(x, df_grouped['FUELCONSUMPTION_CITY'],

bottom=df_grouped['FUELCONSUMPTION_HWY'], color='#1D2F6F')
plt.show()


plt.bar(x, df_grouped['FUELCONSUMPTION_COMB'],

bottom=df_grouped['FUELCONSUMPTION_HWY'] + df_grouped['FUELCONSUMPTION_CITY'],

color='#6EAF46')
plt.show()