import pandas as pd
df=pd.read_csv('iris-parquet.csv')
print(df.to_string())
print(df.head(3))
df=df.drop_duplicates()
print(df.head())
print(df.describe())

import matplotlib.pyplot as plt
import seaborn as sns
df.plot(kind='hexbin',x='petal.width',y='petal.length')
plt.show()
df.plot(kind='hist',x='petal.width',y='petal.length')
plt.show()
df.plot(kind='bar',x='petal.width',y='petal.length')
plt.show()
df.plot(kind='line',x='petal.width',y='petal.length')
plt.show()


