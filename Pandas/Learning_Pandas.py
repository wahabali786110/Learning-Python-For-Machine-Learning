import numpy as np
import pandas as pd
# 1. Series

# Creating Series using List and Dictionary
# List:
# marks=[87,65,98,100,33]
# subjects=['Maths','PS','AI','Python','DWH']

# marks_series=pd.Series(marks, index=subjects,name='Wahab ke marks')
# print(marks_series)

# Dict:
# marks={
#     'Maths':87,
#     'PS':65,
#     'AI':98,
#     'Python':100,
#     'DWH':33
# }

# marks_series=pd.Series(marks,name="Wahab ke marks")
# print(marks_series)

# Series Attributes:
# print(marks_series.size)
# print(marks_series.dtype)
# print(marks_series.values)
# print(marks_series.index)
# print(marks_series.name)
# print(marks_series.is_unique)

# Important method of pandas: read_csv: Use it to read datasets
# subs=pd.read_csv('subs.csv').squeeze()
# print(subs)

# 2 columns
vk=pd.read_csv('kohli_ipl.csv',index_col='match_no').squeeze()
# print(vk)

# movies=pd.read_csv('bollywood.csv',index_col='movie').squeeze()
# print(movies)

# Series Methods: 
# 1. Head and Tail: Extracts first five or last rows. Also we can specify value for how much rows
movies=pd.read_csv('bollywood.csv',index_col='movie').squeeze()
# print(movies.head())
# print(movies.tail())

# print(movies.head(10))
# print(movies.tail(10))

# Sample: Extracts any single random row from the whole dataset. If we specify value than extracts more 
# rows according to the value
# print(movies.sample())
# print(movies.sample(5))

# Value Count: Counts the number of times values appeared in the series
# print(movies.value_counts())

# sort_values: It sorts the values of the series
# vk=pd.read_csv('kohli_ipl.csv',index_col='match_no').squeeze()
# Virat's highest score
# print(vk.sort_values(ascending=False).head(1).values[0])

# sort_index: Sorts index
# movies=pd.read_csv('bollywood.csv',index_col='movie').squeeze()
# sorted_names=movies.sort_index()
# print(sorted_names)

# Series Math Methods:
# 1. Sum, Product
subs=pd.read_csv('subs.csv').squeeze()
# print(subs.sum())
# print(subs.prod())

# # 2. mean, median, mode, std, var
# print(subs.mean())
# print(vk.median())
# print(movies.mode())

# # 3. min, max
# print(subs.min())
# print(subs.max())

# # 4. Describe
# print(subs.describe())

# astype, between, clip, drop_duplicates, duplicated, isnull, dropna, fillna, isin, apply, copy

# print(vk.astype('int16'))

# print(vk[vk.between(51,99)])

# print(subs.clip(100,200))

series=pd.Series([1,1,2,2,3,3,4,4])
# print(series)
# print(series.drop_duplicates(keep='last'))

nan_series=pd.Series([1,2,3,np.nan,5,6,np.nan,8,9,np.nan])
# print(nan_series.isnull().sum())

# print(nan_series.fillna(nan_series.median()))

# print(nan_series.dropna())

# print(vk[vk.isin([49,99])])

# Apply very useful method we can add our own logic here
print(movies.apply(lambda x:x.split()[0].upper()))

print(subs.apply(lambda x:"Good day" if x > subs.mean() else "Bad Day"))