     # **************************** Tuples ****************************************
# Task 1

# test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
# new_list=[]

# for tups in test_list:
#     key=tups[0]
#     value=tups[1]

#     found=False
#     for groups in new_list:
#         if groups[0]==key:
#             groups.append(value)
#             found=True
#             break
         
           

#     if not found:
#         new_list.append([key,value])

# final_list=[tuple(group) for group in new_list]
        


# print(final_list)

# Task 2
# t1 = (1,2,3)
# t2 = (1,2,3)

# if t1==t2:
#     print("t1 and t2 are same.")
# else: print("t1 and t2 are not same")

# Task 3
# tup=(1, 5, 7, 8, 10)

# sum_tuple=()

# for i in range(len(tup)):
#     if i==0:
#         sum=tup[i]*tup[i+1]
#     elif i==len(tup)-1:
#         sum=tup[i]*tup[i-1]
#     else:
#         sum=tup[i-1]*tup[i]+tup[i]*tup[i+1]
        
#     sum_tuple+=(sum,)

   
# print(sum_tuple)

# Task 4
# list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]

# sum_list=0
# sum_set=0
# sum_tuple=0
# for items in list1:
#     if isinstance(items,list):
#         sum_list+=1
#     elif isinstance(items,set):
#         sum_set+=1
#     elif isinstance(items,tuple):
#         sum_tuple+=1

# print("List-",sum_list)

# print("Set-",sum_set)

# print("tuple-",sum_tuple)

# Task 5

# n=int(input("Enter no: of records: "))
# list1=[]
# i=0
# while i<n:
#     print("Enter Details of student no: {}".format(i+1))
#     name=input("Enter the name of student: ")
#     higher=input("Enter the higher education: ")
#     skill=input("Enter the skill of student: ")
#     year=input("Enter the year of graduation: ")

#     tup=(name,higher,skill,year)
#     list1.append(tup)
#     i+=1
# print()
# print("Enter Job requirements")
# pri_skill=input("Enter the skill you want: ")
# high_edu=input("Enter the highest edu you want: ")
# gradu_year=input("Enter the graduation year you want: ")

# Flag=False
# for tups in list1:
#     if tups[2]==pri_skill and tups[1]==high_edu and tups[3]==gradu_year:
#         print(tups)
#         Flag=True


# if not Flag:
#     print()
#     print("No such candidate!")

        
     # **************************** Sets ****************************************
        
# Task 1
# ar1 = [1, 5, 10, 20, 40, 80]
# ar2 = [6, 7, 20, 80, 100,10]
# ar3 = [3, 4, 15, 20, 30, 70, 80, 120]


# set1=set()
# set2=set()
# set3=set()
# list1=[]

# set1.update(ar1)
# set2.update(ar2)
# set3.update(ar3)

# common_eleset=set1&set2&set3
# for items in common_eleset:
#     list1.append(items)
# print(list1)

# Task 2
# Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"

# set1=set(Str1)
# count=0

# for chars in set1:
#     if chars in "aeiouAEIOU":
#         count+=1

# print("No: of unique vowels-{}".format(count))

# Task 3
# str1 = input("Enter the string: ")
# set1=set(str1)

# if 0<len(set1)<=2:
#     print("It is binary")
# else:
#     print("It is not binary")

# Task 4

# list1=[[1, 2, 2, 4, 3, 6],
#        [5, 1, 3, 4],
#        [9, 5, 7, 1],
#        [2, 4, 1, 3]]

# union_set=set()

# for items in list1:
#     union_set|=set(items)

# print(list(union_set))

# Task 5
lst1 = {15, 9, 10, 56, 23, 78, 5, 4, 9}
lst2 = {9, 4, 5, 36, 47, 26, 10, 45, 87}

list3=[item for item in lst1&lst2]

print(list3)


