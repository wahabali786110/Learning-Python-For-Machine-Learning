import pandas as pd
import numpy as np

# Task 1
# empty_series=pd.Series(dtype='object')
# print(empty_series)

# Task 2
# np.random.seed(42)
# series1=pd.Series(np.random.randint(1,50,8))
# series2=pd.Series(np.random.randint(1,50,8))
# print(series1.add(series2, fill_value=0))

# print(series1.sub(series2, fill_value=0)) 
# print(series1.mul(series2, fill_value=1)) 
# print(series1.div(series2, fill_value=1))

# Task 3
# series1=pd.Series([2, 4, 6, 8, 10])
# series2=pd.Series([1, 3, 5, 7, 10])
# print(series1==series2,end="\n\n")
# print(series1>series2,end="\n\n")
# print(series1<series2,end="\n\n")
# print(series1!=series2,end="\n\n")

# Task 4
# def convert_series_datatype(series,datatype):
#     converted_series=pd.to_numeric(series,errors='coerce')
#     converted_series=converted_series.astype(datatype)
#     return converted_series

# series = pd.Series([1,2,'Python', 2.0, True, 100])
# print(convert_series_datatype(series,'float32'))

# Task 5
# batsman_runs=pd.read_csv('batsman_runs_series.csv',index_col='batter').squeeze()

# # 1:
# most_runners=batsman_runs.sort_values(ascending=False).head(10)
# print(most_runners,end="\n\n")

# # 2:
# having_runs_above_3000=batsman_runs[batsman_runs>3000].size
# print(having_runs_above_3000,end="\n\n")

# # 3:
# having_runs_above_mean=batsman_runs[batsman_runs>batsman_runs.mean()].size
# print(having_runs_above_mean)

# Task 6
items=pd.read_csv('items.csv',index_col='item_name').squeeze()

# 1:
nan_values=items.isnull().sum()
# print("No of nan values: ",nan_values)

# 2:
cleaned_items=items.str.replace("$","")

usd_prices=pd.to_numeric(cleaned_items,errors='coerce')
prices_in_pkr=usd_prices*290

# 3:
prices_in_pkr=prices_in_pkr.astype('float')

# 4:
prices_in_pkr.fillna(prices_in_pkr.mean())

# Task 6: Part 2

# 1:
print(prices_in_pkr.mean())

# 2:
print(prices_in_pkr.quantile([0.30,0.06]))

# 3:
import matplotlib.pyplot as plt
prices_in_pkr.plot(kind='hist',bins=50)
plt.show()

# 4:
print(prices_in_pkr.between(1000,2000).sum())
