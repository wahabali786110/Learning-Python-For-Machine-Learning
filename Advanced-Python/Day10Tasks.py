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
class Person:
    def __init__(self,name,age,gender):
        self.age=age
        self.name=name
        self.gender=gender

person=Person('Wahab',22,'male')

# def show(person):
#     if isinstance(person,Person):
#         return {'name':person.name,'age':person.age,'gender':person.gender}
    
# with open('demo.json','w') as f:
#     json.dump(person,f,default=show,indent=4)

# Deserialization process will be similiar

# How to dump your own class object to json file?(object will be passed using this)
import pickle

with open('p.pkl','wb') as f:
    pickle.dump(person,f)

with open('p.pkl','rb') as f:
    q=pickle.load(f)

print(q.name)



