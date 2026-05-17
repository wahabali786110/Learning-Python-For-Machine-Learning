# Task 1

# L1=[1,2,3,4]
# L2=[5,6,7,8]

# L3=[i*j for i in L1 for j in L2]

# print(L3)

# Task 2

# list1 = ["M", "na", "i", "Kh"]
# list2 = ["y", "me", "s", "an"]

# list3=list(zip(list1,list2))
# print(list3)

# Task 3

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)

# print(list1)

# Task 4
# candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
# no_of_items = [10,20,34,74,32]

# list3=[i+"-"+str(j) for i,j in zip(candy_list,no_of_items)]

# for item in list3:
#     print(item)

# Task 5

# list1 = [1,2,3,4,5,6]
# sum=0

# sum_list=[]

# for i in range(len(list1)):
#     if i == 0:
#         sum+=list1[i]
#         sum_list.append(list1[i])
#     else:
#         sum+=list1[i]
#         sum_list.append(sum)

# print(sum_list)

# Task 6
# list1= [2,4,6,10,1]
# sum=0
# sum_list=[]

# for i in range(len(list1)):
#     for j in range(len(list1)):
#         if list1[i]<=list1[j]:
#             sum+=list1[j]
    
#     sum_list.append(sum)
#     sum=0

# print(sum_list)

# Task 7

# num1 = [23,45,67,78,89,34]
# num2 = [34,89,55,56,39,67]

# list1=[]

# for num in num1:
#     if num in num2:
#         list1.append(num)

# print(sorted(list1))

# Task 8
# list1=['CampusX is a channel', 'for data-science', 'aspirants.']

# splitted_list=[]

# for i in range(len(list1)):
#     splitted_list.extend(list1[i].split())

# print(splitted_list)

# Task 9

# matrix=[['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]

# words=[]

# for letter_items in matrix:
#     word="".join(letter_items)

#     words.append(word)

#     final_str=" ".join(words)

# print(word)
# print(words)
# print(final_str)

# Task 10
# list1=['campusxIs', 'bestFor', 'dataScientist']

# new_list=[]

# for word in list1:
#     new_word=''

#     for char in word:
#         if char.isupper():
#             new_word+=" "+char
#         else:
#             new_word+=char

#     new_list.append(new_word)

# print(new_list)

# Task 11

# list1=[1,2,3,4,5,1]
# list2=[2,3,5,7,8]

# list3=[]

# for i in list1:
#     if i not in list3:
#         list3.append(i)

# for i in list2:
#     if i not in list3:
#         list3.append(i)

# print(list3)

# Task 12

# list1=[[1,2,3],[4,5,6],[7,8,9]]
# list2=[]

# for nums in list1:
#     list2.append(max(nums))
    
# print(list2)    

# Task 13

# list1=[[(j*3)+i for i in range(3)] for j in range(3)]
# print(list1)

# Task 14
# matrix = [
# [1,2,3],
# [4,5,6],
# [7,8,9]
# ]

# new_list=[]

# for i in range(len(matrix)):
#     extra_list=[]
#     for row in matrix:
#         extra_list.append(row[i])
#     new_list.append(extra_list)

# List Comprehension
# transpose_matrix=[[row[i] for row in matrix] for i in range(len(matrix))]

# print(transpose_matrix)

# Task 15
matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

flatten_list=[item for row in matrix for item in row]

print(flatten_list)