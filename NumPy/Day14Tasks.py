import numpy as np
# Task 1
# a=35
# arr=np.array( [10, 17, 24, 31, 38, 45, 52, 59])

# distances=np.abs(arr-a)

# nearest_index=np.argmin(distances)

# print(arr[nearest_index])

# Task 2
# arr=np.array([1, 2, 3, 4, 5, 6, 7, 9])
# arr[(arr%3==0) | (arr%5==0)]=0
# print(arr)

# Task 3
# arr = np.arange(10)
# arr[[0,3,4,9]]*=2
# print(arr)

# arr2=np.array([1,2,3])
# pattern=arr2[[0,0,0,1,1,1,2,2,2]]
# print(pattern)

# Task 4
# arr=np.array([[1,2,np.nan],[4,2,6],[np.nan,np.nan,5]])
# valid_numbers=arr[~np.isnan(arr)]

# values,count=np.unique(valid_numbers,return_counts=True)

# most_common=values[np.argmax(count)]
# arr[np.isnan(arr)]=most_common
# print(arr)

# Task 5
# arr=np.array([[3, 2, np.nan, 1],
#           [10, 12, 10, 9],
#           [5, np.nan, 1, np.nan]])

# nan_values=np.isnan(arr)
# print(nan_values)

# arr=np.nan_to_num(arr)
# print(arr)

# Task 6
# x = np.array([1,2,3,4]).reshape((-1, 1))
# y = np.array([5,6,7])

# C=1/(x-y)
# print(C)

# Task 7
# import matplotlib.pyplot as plt

# x=np.linspace(-10,10,100)
# # y=(np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
# y=np.tanh(x)

# plt.plot(x,y)
# plt.show()

# Task 8
# import matplotlib.pyplot as plt

# x=np.linspace(-2,10,100)
# y=np.sqrt(36-((x-4)**2))+2

# plt.plot(x,y)
# plt.axis('equal')
# plt.show()

# Task 9
def check_broadcast(shape_a,shape_b):

    for dim_a,dim_b in zip(reversed(shape_a),reversed(shape_b)):
        if dim_a!=dim_b and dim_a!=1 and dim_b!=1:
            return False
        
    return True

a = (3, 2, 2)
b = (2, 2)
print(f"Can {a} and {b} broadcast? -> {check_broadcast(a, b)}")
