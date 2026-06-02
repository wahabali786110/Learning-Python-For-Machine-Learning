import numpy as np

# Boolean Indexing: We can specify condition in the index to fetch that specific items.
# a=np.random.randint(1,100,24).reshape(6,4)
# print(a)
# print(a[a>50])
# print(a[a%2==0])
# print(a[(a>50) & (a%2==0)]) # We can also use two conditions like this
# & this is bitwise and used when dealing with boolean values.
# and: this is logical and used in python

# Broadcasting: Broadcasting is NumPy's built-in mechanism that automatically "stretches" 
# smaller arrays to match the dimensions of larger arrays so you can perform fast, 
# element-wise math without writing slow for loops.

# Rules:
# Pad the Left: If the arrays have a different number of dimensions,
#  add 1s to the left side of the smaller shape.

# Stretch the 1s: If any dimension is size 1, stretch it to match the size of the other array.

# Crash on Conflict: If the dimensions still don't match and neither is a 1, throw an error.

# Mathematical function
# 1: Sigmoid

# def sigmoid(array):
#     return 1/(1+np.exp(-array))

# a=np.arange(10)
# print(sigmoid(a))

# 2: Mean Squared Error
# def mean_squared_error(y_true,y_predict):

#     if y_true.shape!=y_predict.shape:
#         raise ValueError(f"Shape mismatch: y_true is {y_true.shape} but y_pred is {y_predict.shape}")
    
#     return np.mean((y_true-y_predict)**2)

    
# y_true=np.array([300,400,500])
# y_predict=np.array([300,0,500])

# print(mean_squared_error(y_true,y_predict))

# 3: Binary Cross Entropy

# def binary_cross_entropy(y_true,y_predict):

#     if y_true.shape!=y_predict.shape:
#         raise ValueError(f"Shape mismatch: y_true is {y_true.shape} but y_pred is {y_predict.shape}")
    
#     epsilon=1e-15
#     y_predict_clipped=np.clip(y_predict,epsilon,1-epsilon)

#     first_term=(y_true*np.log(y_predict_clipped))
#     second_term=(1-y_true)*np.log(1-y_predict_clipped)
#     bse=-np.mean(first_term+second_term)

#     return bse

# true_labels = np.array([1, 0, 1])
# ai_predictions = np.array([0.90, 0.10, 0.10])

# loss = binary_cross_entropy(true_labels, ai_predictions)
# print(f"Binary Cross Entropy Loss: {loss}")

# # Working with missing values
# a=np.array([1,2,3,4,np.nan,6])
# print(a[~np.isnan(a)]) # Here ~ is working like a NOT operation, Converts True to False and Fetch False values

# Plotting Graphs:
import matplotlib.pyplot as plt
# For straight line: y=x
# x=np.linspace(-10,10,100)
# y=x
# plt.plot(x,y)
# plt.show()

# For parabola: y=x^2
# x=np.linspace(-10,10,100)
# y=x**2
# plt.plot(x,y)
# plt.show()

# For Sin Curves: y=sin(x)
# x=np.linspace(-10,10,100)
# y=np.sin(x)
# plt.plot(x,y)
# plt.show()

# For  y= xlog(x)
# x=np.linspace(-10,10,100)
# y=x*np.log(x)
# plt.plot(x,y)
# plt.show()

# For sigmoid: y=1/1+e^-x
# x=np.linspace(-10,10,100)
# y=1/(1+np.exp(-x))
# plt.plot(x,y)
# plt.show()

# 3D Graph:

z_line = np.linspace(0, 15, 1000)
x_line = np.sin(z_line)
y_line = np.cos(z_line)


fig = plt.figure(figsize=(8, 8))

ax = fig.add_subplot(projection='3d')


ax.plot(x_line, y_line, z_line, color='blue', linewidth=2)


ax.set_title("3D Flight Path (Spiral)")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis (Altitude)")

plt.show()
