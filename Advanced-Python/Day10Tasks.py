# File handling

# with open('sample.txt','w') as f:
#     f.write("Hello!\n")


# L=['How are you?\n','I am fine\n','What about you?\n']

# with open('sample.txt','a') as f:
#     f.writelines(L)

# with open('sample.txt','r') as f:
#     # Prints only one line
#     print(f.readline())

# with open('sample.txt','r') as f:
#     # Prints all lines
#     print(f.read())

# with open('sample.txt','r') as f:
#     # Way to printing all lines using readLine()
#     while True:
#        data=f.readline()
#        if data=='':
#            break
#        else:
#            print(data,end='')

# Working with binary files
# with open('PSP-min.png','rb') as f:
#     with open('PSP-min_copy.png','wb') as g:
#         g.write(f.read())


# Points to remember: We use f.tell() for checking the current index of the read function or 
# write funcion and we use f.seek() for changing to index to any point by sending argument eg. 10, 20

# JSON-> Java Script On Notation

# Serialization: Converting python data type to JSON format
# import json
# d={'name':'Wahab','age':21,'gender':'male'}

# with open('demo.json','w') as f:
#     json.dump(d,f,indent=4)

# Deserialization: Converting JSON to python data type
# with open('demo.json','r') as f:
#     d=json.load(f)
#     print(d)
#     print(type(d))

# Using this because normal file handlers can't deal with other data types except strings.

# How to dump your own class object to json file?(object will not be passed using this)
# import json
# class Person:
#     def __init__(self,name,age,gender):
#         self.age=age
#         self.name=name
#         self.gender=gender

# person=Person('Wahab',22,'male')

# def show(person):
#     if isinstance(person,Person):
#         return {'name':person.name,'age':person.age,'gender':person.gender}
    
# with open('demo.json','w') as f:
#     json.dump(person,f,default=show,indent=4)

# Deserialization process will be similiar

# How to dump your own class object to json file?(object will be passed using this)

# import pickle
# This will convert the object to binary stream.
# with open('p.pkl','wb') as f:
#     pickle.dump(person,f)

# # This will convert the object to object hierarchy from binary stream
# with open('p.pkl','rb') as f:
#     q=pickle.load(f)

# print(q.name)

# Task 1
# def get_final_line(filename):
#     with open(filename,'r') as f:
#         data=f.readlines()
#         return data[-1]
    
# L=['Hello\n','How are you?\n',"I am fine.\n","What about you?"]
# with open('Day10Task1.txt','w') as f:
#     f.writelines(L)

# print(get_final_line('Day10Task1.txt'))

# Task 2
# dict1={}

# with open('Day10Task1.txt','r') as f:
#     while True:
#         line=f.readline()
#         if line=="":
#             break
#         else:
#             for char in line.lower():
#                 if char in dict1 and char in "aeiou":
#                     dict1[char]+=1
#                 elif char not in dict1 and char in "aeiou":
#                     dict1[char]=1

# print(dict1)

# Task 3
# total=0
# list2=[]
# with open('Day10Task3.txt','r') as f:
#     for line in f:
#         parts=line.split()
#         if len(parts)==2:
#             first_num=int(parts[0])
#             second_num=int(parts[1])

#             product=first_num*second_num
#             total+=product
#             new_line=f"{first_num}\t{second_num}\t{product}\n"
#             list2.append(new_line)

# with open('Day10Task3.txt','w') as f:
#     f.writelines(list2)
#     f.write(f"Total\t{total}")

# Task 4

# def line_wise_reverse(first_file,second_file):
#     reversed_line=[]
#     with open(first_file,'r') as f:
#         for line in f:
#             clean_line=line.rstrip('\n')
#             new_str=clean_line[::-1]
#             reversed_line.append(new_str+"\n")

#     with open(second_file,'w') as f:
#         f.writelines(reversed_line)
        

# line_wise_reverse('Day10Task4.txt','Day10Task4-2.txt')

# Task 5
# import json
# strings = """Alice was beginning to get very tired of sitting by her sister
#             on the bank, and of having nothing to do:  once or twice she had
#             peeped into the book her sister was reading, but it had no
#             pictures or conversations in it, `and what is the use of a book,'
#             thought Alice `without pictures or conversation?'

#             So she was considering in her own mind (as well as she could,
#             for the hot day made her feel very sleepy and stupid), whether
#             the pleasure of making a daisy-chain would be worth the trouble
#             of getting up and picking the daisies, when suddenly a White
#             Rabbit with pink eyes ran close by her.

#             There was nothing so VERY remarkable in that; nor did Alice
#             think it so VERY much out of the way to hear the Rabbit say to
#             itself, `Oh dear!  Oh dear!  I shall be late!'  (when she thought
#             it over afterwards, it occurred to her that she ought to have
#             wondered at this, but at the time it all seemed quite natural);
#             but when the Rabbit actually TOOK A WATCH OUT OF ITS WAISTCOAT-
#             POCKET, and looked at it, and then hurried on, Alice started to
#             her feet, for it flashed across her mind that she had never
#             before seen a rabbit with either a waistcoat-pocket, or a watch to
#             take out of it, and burning with curiosity, she ran across the
#             field after it, and fortunately was just in time to see it pop
#             down a large rabbit-hole under the hedge."""

# dict1={}

# list1=strings.lower().split()
# word_list = ['alice', 'wonder', 'natural','so','her']
# for word in list1:
#     clean_word = word.strip(".,;:!'\"()-`")
#     if clean_word in dict1:
#         dict1[clean_word]+=1
#     else:
#         dict1[clean_word]=1

# with open('words_dict_task_5.json','w') as f:
#     json.dump(dict1,f,indent=4)

# with open('words_dict_task_5.json','r') as f:
#     dict1=json.load(f)
#     for item in word_list:
#         if item in dict1:
            
#             print(item,dict1.get(item))
        

# Task 6
# def length_str(str1):
#     if str1 =="":
#         return 0
#     else:
#         return 1+length_str(str1[1:])



# str1="abcd"

# print(length_str(str1))

# Task 7
# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)

# print(gcd(16,25))

# Task 8
# def edit_distance(s,t):
#     if len(s)==0:
#         return len(t)
#     elif len(t)==0:
#         return len(s)
#     else:
#         cost=0

#         if s[-1]!=t[-1]:
#             cost=1

#         d1=edit_distance(s[:-1],t)+1
#         d2=edit_distance(s,t[:-1])+1
#         d3=edit_distance(s[:-1],t[:-1])+cost

#         return min(d1,d2,d3)

# print(edit_distance('kitten','sitting'))

# Task 9

def decimal_binary(num):
    if num ==0 or num==1:
        return str(num)
    else:
        remainder=str(num%2)
        other_numbers= decimal_binary(num//2)
        return other_numbers + remainder
    
print(decimal_binary(10))