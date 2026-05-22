# Task 1 and 2
# class Person:
#     def __init__(self,name,city,state,age):
#         self.name=name
#         self.__city=city
#         self.state=state
#         self.__age=age

#     def address(self):
#         print(f"{self.name}, {self.__city}, {self.state}")

# p1=Person('Wahab',"Sujawal",'Sindh',21)

# print(Person.__dict__)
# print()
# print()
# print(p1.__dict__)

# Task 3
# def gcd_with_counter(a, b, calls=1):
#     if b == 0:
#         return a, calls
#     else: 
#         return gcd_with_counter(b, a % b, calls + 1)

# result, total_calls = gcd_with_counter(5, 10)

# print(f"gcd(5,10) -> result in {result} as gcd and function call {total_calls}")

# Task 4
# class MyEnumerate:
#     def __init__(self,data):
#         self.data=iter(data)
#         self.index=0

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         item =next(self.data)
#         current_index=self.index

#         self.index+=1

#         return(current_index,item)
    


# try:
#     a=MyEnumerate([1,2,3,4,5,6,7])
#     for index,letter in a:
#         print(index,letter)
# except TypeError:
#     print("Use only iterable objects")

# Task 5

# class Circle:
#     def __init__(self,data,max):
#         self.data=data
#         self.max=max
#         self.index=0


#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.index>=self.max:
#             raise StopIteration
        
#         safe_index=self.index % len(self.data)

#         item=self.data[safe_index]
#         self.index+=1

#         return item
    

# a=Circle('abcd',7)

# print(list(a))

# Task 6
# import time
# def My_Generator(data):
#     last_time=None
#     for i in data:
#         start_time=time.time()
#         if last_time is None:
#             time_elasped=0.0
#         else:
#             time_elasped=start_time-last_time

#         last_time=time.time()   

#         yield (time_elasped,i)

        

# gen=My_Generator('abcd')

# for i in gen:
#     print(i)
#     time.sleep(2)


# Task 7
# def bold(func):
#     def wrapper():
#         original_text=func()
#         return f"<b>{original_text}</b>"
        
#     return wrapper

# def itallic(func):
#     def wrapper():
#         original_text=func()
#         return f"<i>{original_text}</i>"
        
#     return wrapper

# def under_line(func):
#     def wrapper():
#         original_text=func()
#         return f"<u>{original_text}</u>"
        
#     return wrapper
# @under_line
# @itallic
# @bold
# def hello():
#     return "Hello World"

# print(hello())

# Task 8
# def printer(func):
#     def wrapper(*args,**kwargs):
#         value=func(*args,**kwargs)
#         if value is not None:
#          print(value)
#     return wrapper

# @printer
# def greet():
#     return 5+6

# @printer
# def print_number(num,num2):
#    return num+num2

# greet()
# print_number(5,8)

# Task 9
# def My_Decorator(func):
#     def wrapper(*args,**kwargs):
#         func(*args,**kwargs)
#         func(*args,**kwargs)
#     return wrapper

# @My_Decorator
# def hello(string):
#     print(string)


# hello("Hellooo")

# Task 10

def double_value(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)*2

    return wrapper

@double_value
def add(a,b):
    return a+b


assert(add(2,3))==10, "Double_value decorator is broken my deer :("

print("Decorator is working completely fine.")