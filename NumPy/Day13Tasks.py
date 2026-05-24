import numpy as np

# Task 1
# a1=np.zeros(10,dtype=np.int32)
# a1[4]=1
# print(a1)

# Task 2
# a=int(input('Enter first number: '))
# b=int(input('Enter second number: '))

# a1=np.random.random((a,b))
# avg=np.mean(a1)

# print(a1,end="\n\n")
# print("Avg:",avg)

# Task 3
# def create_2d_array(a,b):
#     a1 = np.ones((a,b),dtype=np.int32)
#     a1[1:-1,1:-1]=0
#     return a1

# print(create_2d_array(6,6))

# Task 4
# a1=np.linspace(0,1,10)[1:-1]
# print(a1)

# Task 5
# a1=np.eye(4,4)
# print(a1)

# Task 6
# a1=np.zeros((5,5))+np.arange(5)
# print(a1)

# Task 7
# a=np.random.random((10,2))*100
# a=np.round(a).astype(np.int32)
# print(a)
# point=np.array([2,3])

# diff=a-point

# squared=diff**2
# summed=np.sum(squared,axis=1)

# distances=np.sqrt(summed)

# distances=distances.astype(np.int32)
# print(distances)

# Task 8
# a1=np.arange(336).reshape(6,7,8)
# print(a1[1,5,3])

# It tells the indexes of the element you are looking for
# coordinates=np.unravel_index(99,(6,7,8))
# print(coordinates)

# Task 9
# lis1=input().split()
# a=np.array(lis1,dtype=float)[::-1]
# print(a)

# Task 10
# count =0
# a1=np.array([[1,2,3,4],[5,6,7,8]])


# count=len(np.ravel(a1))

# print(count)

# Task 11
# from math import e
# def softmax(array):
#     if not isinstance(array,np.ndarray):
#         raise TypeError("Input must be a NumPy array.")
#     elif array.ndim!=1:
#         raise ValueError("Input must be a 1d array.")
#     else:
#         exp=np.exp(array)
#         total=np.sum(exp)
#         softmax_probabilities =exp/total

#         return softmax_probabilities

# a1=np.array([86.03331084, 37.7285648,  48.64908087, 87.16563062, 38.40852563, 37.20006318])

# try:
#     a=softmax(a1)
# except TypeError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# else:
#     print(a)

# Task 12
# def vertical_stacks(*args):
#     if not all(isinstance(item,np.ndarray) for item in args):
#         raise TypeError("Input must be numpy arrays")
#     else:
#         a=np.vstack(args)

#         return a
    
# a=np.arange(10).reshape(2,5)
# b=np.arange(10,20).reshape(2,5)

# try:
#     stacked=vertical_stacks(a,b)
# except TypeError as e:
#     print(e)
# else:
#     print(stacked)

# # Task 13
# def date_array(start,end):
#     if not isinstance(start,str) or not isinstance(end,str):
#         raise TypeError("Input should be strings")
#     else:
#         start=np.datetime64(start)
#         end=np.datetime64(end)+np.timedelta64(1,'D')

#         a=np.arange(start,end)
#         return a.astype(str)

# try:
#     a= date_array('2020-09-15','2020-09-25')
# except TypeError as e:
#     print(e)
# else:
#     print(a)

# Task 14
# a=np.arange(12,24).reshape(4,3)
# avg=np.mean(a,axis=1,keepdims=True)
# a=a-avg
# print(a)

# Task 15
# a=np.arange(12,24).reshape(4,3)
# a[:,[0,1]]=a[:,[1,0]]
# print(a)

# Task 16
# a=np.arange(12,24)
# a[a%2!=0]=-1
# print(a)

# Task 17
# a=np.array([6,3,1,5,8])
# b=np.array([3,2,1,7,2])

# max_array=np.maximum(a,b)
# print(max_array)

# Task 18
# arr1=np.random.randint(low=1, high=10000, size=40).reshape(8,5)

# alternativecol_arr=arr1[:,::2]
# print("Original Array:\n",arr1,end="\n\n")
# print("Alternative Column:\n",alternativecol_arr,end="\n\n")


# x_min=np.min(arr1)
# x_max=np.max(arr1)

# numertaor= arr1-x_min
# denominator=x_max-x_min


# normalized_arr=numertaor/denominator

# print("Normalized Arr:\n",normalized_arr)

# Task 19
# a=np.array([1,2,3])
# print(a)
# pattern_1=np.repeat(a,3)
# pattern_2=np.tile(a,3)

# a=np.concatenate((pattern_1,pattern_2))
# print(a)

# Task 20
def nth_largest(arr,n):
    if n>len(arr):
        raise ValueError("N cannot be larger than array size")
    else:
        sorted_array=np.sort(arr)
        
        target_value=sorted_array[-n]
        return target_value

arr1=np.array([12,34,40,7,1,0])
try:
    print(nth_largest(arr1,3))
except ValueError as e:
    print(e)

