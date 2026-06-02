# Imporant Tricks of NumPy
# Important Methods:
# Sort: np.sort()
import numpy as np
# a=np.random.randint(10,100,10)
# print(a)
# print(np.sort(a))
# print("Descending: ",np.sort(a)[::-1])

# Append: np.append()
# a=np.array([1,2,3,4,5,6])
# print(np.append(a,200))
# a1=np.array([1,2,3,4,5,6,7,8,9,10,11,12]).reshape(4,3)
# print(np.append(a1,np.ones((a1.shape[0],1)),axis=1))

# Concatenate: np.concatenate
# a=np.arange(6).reshape(2,3)
# b=np.arange(6,12).reshape(2,3)

# print(np.concatenate((a,b),axis=0),)

# Where: np.where(condition,true,false)
# a=np.array([45,23,12,67,98,2,54,6,2,3,8,87,43,91,1,76,65,58])
# Change number to 0 where a is > 50
# print(np.where(a>50,0,a))

# Cumulative sum: np.cumsum()
# a=np.array([45,23,12,67,98,2,54,6,2,3,8,87,43,91,1,76,65,58])
# print(np.cumsum(a))

#  Cumulative product: np.cumprod()
a=np.array([45,23,12,67,98,2,54,6,2,3,8,87,43,91,1,76,65,58])
print(np.cumprod(a))
