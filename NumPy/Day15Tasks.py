import numpy as np
# Task 1
# np.random.seed(43)
# arr=np.random.randint(0,100,12).reshape(4,3)
# print(arr,end="\n\n")
# # Part 1
# # print(np.sort(arr),end="\n\n")
# # 
# # Part 2
# # second_col=arr[:,1]
# # indexes=np.argsort(second_col)
# # print(arr[indexes],end="\n\n")
# # 
# # Part 3
# # max=np.max(arr,axis=1)
# # indexes=np.argsort(max)
# # print(arr[indexes],end="\n\n")

# # Part 4
# flatten_list=np.ravel(arr)
# print(np.sort(flatten_list))

# Task 2
# np.random.seed(42)
# arr=np.random.randint(0,100,20).reshape(5,4)
# # Part 1
# extra_subject = np.array([41, 87, 72, 36, 92]).reshape(5,1)
# arr=np.append(arr,extra_subject,axis=1)
# print(arr,end="\n\n")

# # Part 2
# rec1 = np.array([77, 83, 98, 95, 89]).reshape(1,5)
# rec2 = np.array([92, 71, 52, 61, 53]).reshape(1,5)

# arr=np.concatenate((arr,rec1,rec2))
# print(arr,end="\n\n")

# # Part 3
# col_sum=np.sum(arr,axis=1).reshape(7,1)
# arr=np.append(arr,col_sum,axis=1)
# print(arr,end="\n\n")

# # Part 4
# marks_column=arr[:,-1]
# indexes=np.argsort(marks_column)[::-1]
# arr=arr[indexes]
# print(arr[:2])

# Task 3
# arr = np.array([[1,2,3,3,1,1],
#                 [0,9,1,2,8,8],
#                 [1,2,3,8,8,8],
#                 [1,2,3,3,1,1]])

# column_wise=np.unique(arr,axis=1)
# row_wise=np.unique(arr,axis=0)
# print(row_wise,end="\n\n")
# print(column_wise,end="\n\n")

# Task 4
# arr = np.array([[1,2,3,3,1,1],
#                  [0,9,1,2,8,8],
#                  [1,2,3,8,8,8],
#                  [1,2,3,3,1,1]])

# print(np.flip(arr))

# Task 5

# arr = np.array([[1,2,3,4,5], 
#       [10,-3,30,4,5], 
#       [3,2,5,-4,5], 
#       [9,7,3,6,5]] )
# X=6

# rows=np.any(arr>X,axis=1)
# row_number=np.where(rows)[0]
# print(row_number)

# Task 6
# arr1 = np.arange(3)
# arr2 = np.arange(3,7)
# arr3 = np.arange(7,10)

# flatten_array=np.concatenate((arr1,arr2,arr3))
# print(flatten_array)

# Task 7
# np.random.seed(400)

# arr = np.random.randint(100, 1000, 200).reshape((1, 200))
# print(arr)
# min=np.min(arr)
# max=np.max(arr)

# mask = (arr!=min)&(arr!=max)
# arr=arr[mask]
# print(arr)

# Task 8
# np.random.seed(400)
# arr=np.random.randint(0,1000,100)
# arr=np.clip(arr,100,200)
# arr=np.sort(arr)
# cum_sum=np.cumsum(arr)
# print(cum_sum)

# Task 9
np.random.seed(400)
arr=np.random.rand(100)
arr=np.round(arr,decimals=3)

min_value=np.percentile(arr,0)
if min_value==np.min(arr):
    print(True)

max_value=np.percentile(arr,100)
if max_value==np.max(arr):
    print(True)

difference=np.percentile(arr,51)-np.percentile(arr,50)

print(difference)

