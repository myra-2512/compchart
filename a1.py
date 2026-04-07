import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('gapminder(2007) (1).csv')
print(df.head())
print(df.info())
avg_data = df.groupby('continent')[['life_exp', 'gdp_cap']].mean().reset_index()
print(avg_data)

plt.bar(avg_data['continent'],avg_data['life_exp'],color='teal')
plt.xlabel('Continent')
plt.ylabel('Average Life Expectancy')
plt.show()

plt.bar(avg_data['continent'],avg_data['gdp_cap'],color='orange')
plt.xlabel('Continent')
plt.ylabel('Average GDP per Capita')
plt.show()

sns.countplot(x=df['continent'],palette='winter')
plt.show()