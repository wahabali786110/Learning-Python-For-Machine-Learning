# Task 1
# def unique_items(L):
#     set1=set(L)
#     return set1


# L=[1,2,1,3,3,4,4,5,6,6,7]

# print(unique_items(L))

# Task 2

# def sorted_str(str1):
#     L=str1.split('-')
#     Li=sorted(L)
#     print(L)
#     return "-".join(Li)

# str1="green-red-yellow-black-white"

# print(sorted_str(str1))


# Task 3

# def countUpperAndLower(str1):
#     upper=0
#     lower=0

#     for i in range(len(str1)):
#         if str1[i].isupper():
#             upper+=1
#         elif str1[i].islower():
#             lower+=1

#     print("No: of upper characters: ",upper)
#     print("No: of lower characters: ",lower)




# str1='CampusX is an Online Mentorship Program fOr EnginEering studentS.'
# countUpperAndLower(str1)


# Task 4
# def print_even(L):
#     new_list=[]
#     for item in L:
#         if item%2==0:
#             new_list.append(item)

#     print(new_list)

# L=[1,2,3,4,5,6,7,8,9]
# print_even(L)

# Task 5

# def concate_dict(*args):
#     new_dict={}
#     for key in args:
#         new_dict.update(key)
        

#     print(new_dict)

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}

# concate_dict(dic1,dic2,dic3)

# Task 6
# def most_occurence(str1):
#     lis=str1.split()
#     dict1={}

#     for word in lis:
#         if word in dict1:
#             dict1[word]+=1
#         else:
#             dict1[word]=1
          

#     max_count=0
#     best_word=""

#     for words,count in dict1.items():
#         if count>max_count:
#             max_count=count
#             best_word=words

#     return f'{best_word}->{max_count}'


# str1="hello how are you i am fine thank you hello hello"
# print(most_occurence(str1))

# Task 7
# import math
# def nearest(L,Q):
#     qx,qy=Q

#     min_distance=float('inf')
#     closest_point=None

#     for points in L:
#         px,py=points

#         distance=math.sqrt((px-qx)**2+(py-qy)**2)

#         if distance<min_distance:
#             min_distance=distance
#             closest_point=points

#     return f'Nearest Point->{closest_point}'

# list1=[(2,2),(1,1),(3,3),(4,4)]
# query_point=(0,0)

# print(nearest(list1,query_point))

# Task 8
# def bag_of_words(str1):
#     dict1={}
#     L=str1.split()
#     print(L)
#     for word in L:
#         clean_word=word.strip('.')
#         if word in dict1:
#             dict1[clean_word]+=1
#         else:
#             dict1[clean_word]=1

#     return dict1

# str2=" John likes to watch movies. Mary likes movies too. Mary also likes to watch football games."
# print(bag_of_words(str2))

# Task 9
# list1=[1,2,3]
# list2=[4,5,6]
# list3=[7,8,9]

# combined_list=list(map(lambda x,y,z:x+y+z,list1,list2,list3))
# print(combined_list)

# Task 10
# list1 = [1,2,3,4,5,6]

# new_list=list(map(lambda value,index: value**index,list1,range(len(list1))))

# print(new_list)

# Task 11
# def extract_vowels(str1):

#     vowels=list(filter(lambda char: char in 'aeiou',str1.lower()))

#     return vowels
# str1="Wahab is leaning Python"
# vowels=extract_vowels(str1)
# print(vowels)

# Task 12
# from functools import reduce

# def flat_list(L):

#     flatten_list=reduce(lambda x,y:x+y,L)

#     return flatten_list

# matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# print(flat_list(matrix))

# Task 12
employees = [
    {
        'fname':'Nitish',
        'lname':'Singh',
        'age' : 33,
        'grade':'skilled'
    },
    {
        'fname':'Ankit',
        'lname':'Verma',
        'age' : 34,
        'grade':'semi-skilled'
    },
    {
        'fname':'Neha',
        'lname':'Singh',
        'age' : 35,
        'grade':'highly-skilled'
    },
    {
        'fname':'Anurag',
        'lname':'Kumar',
        'age' : 30,
        'grade':'skilled'
    },
    {
        'fname':'Abhinav',
        'lname':'Sharma',
        'age' : 37,
        'grade':'highly-skilled'
    }
    
]

new_list=list(map(lambda key:key['fname']+" "+key['lname'],list(filter(lambda x:True if x['grade']=='highly-skilled' else False,employees))))
print(new_list)
print(list(filter(lambda x:True if x['grade']=='highly-skilled' else False,employees)))
