# It is used for scientific operations. Creates a numpy array of fixed size with same data type variables.
# They are fast because originally they are from C and integrated to Python
# Best for mathematical operations.
# NumPy is fast data type and have fixed size in the memory

# Creating NumPy Arrays
import numpy as np

# 1D Array
# a=np.array([1,2,3,4])
# print(a)

# 2D Array
# b=np.array([[1,2,3],[4,5,6]],dtype=float)
# print(b)

# 3D Array or Tensor
# c = np.array([
#     [
#         [1, 2, 3], 
#         [4, 5, 6]
#     ],
#     [
#         [7, 8, 9], 
#         [10, 11, 12]
#     ]
# ])
# print(c)

# Creating array with range
# a=np.arange(1,11,2)
# print(a)

# Using reshape along with arange

# b=np.arange(1,13).reshape(3,4)
# print(b)


# Using ones, zeroes and random to initialize numpy array: We pass tuple in the method including rows,cols
# It will create the array according to the rows and cols given in the tuple
# a=np.ones((3,4))
# print(a,end="\n\n")

# b=np.zeros((3,4))
# print(b,end="\n\n")

# c=np.random.random((4,3))
# print(c)

# Using linspace and identity:
# Linspace method: It creates a list of perfectly evenly spaced numbers between a starting point
#  and an ending point.

# a=np.linspace(-10,10,5)
# print(a)

# Identity method: Creates a identity matrix according to the value provided.
# b=np.identity(3)
# print(b)

# Important Attribues
# a1=np.arange(10,dtype=np.int32)
# a2=np.arange(12,dtype=float).reshape(3,4)
# a3=np.arange(8).reshape(2,2,2)

# Tells dimension: (ndim)
# print(a3.ndim)

# Tells shape: Rows and Colums : (shape)
# print(a3.shape)

# Tells size of array: No of elements. (size)
# print(a3.size)

# Tells size of array in terms of memory space. (itemsize)
# print(a2.itemsize)

# Tells the datatype of the elements of the array. (dtype)
# print(a1.dtype)
# print(a2.dtype)
# print(a3.dtype)

# Changing data type of already built array: It creates copy so you have to assign it to variable again.
# Method used is astype():
# a3=a3.astype(np.int32)
# print(a3.dtype)

# Array operations
# a1=np.arange(12).reshape(3,4)
# a2=np.arange(12,24).reshape(3,4)

# Scaler Operations
# Arthimatic
# print(a1*2)
# print(a1+2)
# print(a1-2)
# print(a1/2)

# Relational
# print(a2>12)
# print(a2<15)
# print(a2==15)

# Vector Operation: Possible only when dimension of arrays are same
# print(a1+a2,end="\n\n")
# print(a1*a2,end="\n\n")
# print(a1-a2,end="\n\n")
# print(a1/a2,end="\n\n")
# print(a1**a2,end="\n\n")

# Array Functions:
# a1=np.random.random((3,3))
# a1=np.round(a1*100)

# print(a1,end="\n\n")
# max,min,sum,prod
# print(np.max(a1),end="\n\n")
# print(np.min(a1),end="\n\n")
# print(np.sum(a1),end="\n\n")
# print(np.prod(a1),end="\n\n")

# for each row: axis=1 for each column axis=0
# print(np.max(a1,axis=1),end="\n\n")
# print(np.min(a1,axis=1),end="\n\n")
# print(np.sum(a1,axis=1),end="\n\n")
# print(np.prod(a1,axis=1),end="\n\n")

# If you want to these operation for each column just change the value of axis to 0

# mean,median,std,var: If use axis will check row or column wise.
# if not use axis then will check in whole matrix and pick one
# print(np.mean(a1,axis=1))
# print(np.median(a1,axis=1))
# print(np.std(a1,axis=1))
# print(np.var(a1,axis=1))

# Trignometric Operations
# print(np.sin(a1))
# print(np.cos(a1))
# print(np.tan(a1))

# Array dot product:
# It is possible when columns of first column are equal to the rows of second column
# n*m=n*m -> 3*4=4*3
# here it is possible because of m of 1st and n of 2nd are equal.
# Important point: After dot product dimesnions of new matrix will be: n of 1st matrix and m of 2nd
# 3*4=4*3 possible because col of 1st and row of 2nd are equal. new matrix will be 3*3
# a1=np.arange(12).reshape(3,4)
# a2=np.arange(12,24).reshape(4,3)

# print(np.dot(a1,a2))

# Log and exponent:
# print(np.log(a1))
# print(np.exp(a1))

# round,floor,ceil
# a1=np.random.random((3,3))*100
# print(a1,end="\n\n")
# print(np.round(a1),end="\n\n")
# print(np.floor(a1),end="\n\n")
# print(np.ceil(a1),end="\n\n")



# Learnt indexing and slicing
# a1=np.arange(10)
# a2=np.arange(12).reshape(3,4)
# a3=np.arange(27).reshape(3,3,3)

# print(a3[::2,0,::2])

# How to loop through arrays other than 1d to print all the elements present one by one:
# It will convert any dimension of array into 1d array and then print all the elements
# for i in np.nditer(a3):
#     print(i)

# Transpose and Ravel
# a2=np.arange(12).reshape(3,4)
# Two ways to transpose matrix: 1)np.transpose(a2) and 2) a2.T (Short way)
# print(a2,end="\n\n")
# print(np.transpose(a2),end="\n\n")
# print(a2.T)

# Ravel: Converts any dimension array to 1d array:
# print(np.ravel(a2))

# Stacking and Splitting
a4=np.arange(12).reshape(3,4)
a5=np.arange(12,24).reshape(3,4)

# Horizontal Stacking: Dimensions of the array must be same
print(np.hstack((a4,a5)),end="\n\n")

# Vertical Stacking: Dimensions of the array must be same
print(np.vstack((a4,a5)),end="\n\n")

# Horizontal Splitting:
print(np.hsplit(a5,2),end="\n\n")

# Veritcal Splitting
print(np.vsplit(a4,3),end="\n\n")