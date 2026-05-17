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
list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]

sum_list=0
sum_set=0
sum_tuple=0
for items in list1:
    if isinstance(items,list):
        sum_list+=1
    elif isinstance(items,set):
        sum_set+=1
    elif isinstance(items,tuple):
        sum_tuple+=1

print("List-",sum_list)

print("Set-",sum_set)

print("tuple-",sum_tuple)


