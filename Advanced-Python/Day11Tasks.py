# Task 1
# def function(l: list, s, **args):
#     last_element = l[-1]
    
#     l[int(s)]=10
#     any_element = l[int(s)+10]
#     l[s]=10
    
#     res = sum(l)
    
#     p = args['p']
#     # print(p)
#     return res/last_element * p + any_element


# try:
#     function([1,2,0]*9, 12, p=10)
# except TypeError:
#     print("Typing mistake")
# except IndexError:
#     print("Index is out of bound")
# except ValueError:
#     print("There is an error in the value")
# except KeyError:
#     print("Error in the key of dict")
# except ZeroDivisionError:
#     print("Number can't be divided by zero")
# except Exception as e:
#     print(e)

# Task 2

# l = [{0:2},2,3,4,'5', {5:10}]
# # For calculating sum of above list
# s=0
# for i in range(len(l)):
#     try:
#         s += l[i].get(i)
#     except AttributeError:
#         try:
#             s += l[i]
#         except TypeError:
#              s += int(int(l[i]))


# print(s)

# Task 3

# try:
#     with open('sample1.txt','w') as f:
#         f.write("Hello, Good Morning!!!")
# except IOError:
#         print("IO error")
# except TypeError:
#       print("You can't write other than string!")
# else:
#         print("Successfully written")

# Task 4
# def print_natural():
#     try:
#         i=1
#         while True:
#             print(i,end=" ")
            
#             if i==20:
#                  raise StopIteration
#             i+=1

                
#     except StopIteration as e:
#         print("\nIteration Exceeds")
        
# print_natural()
        

# Task 5
# import random
# random_number=random.randint(1,10)

# class ValueTooSmall(Exception):
#     pass

# class ValueTooLarge(Exception):
#     pass

# class GuessError(Exception):
#     pass

# print("******Welcome to Guess Number game******")
# print("Guess number between 1 and 10")

# while True:
#     try:
        
#         guess_number=int(input("\nGuess the Number: "))

#         if guess_number<1:
#             raise GuessError("Guess cannot be less than 1")
        
#         if guess_number==random_number:
#             print("You won")
#             break
#         elif guess_number<random_number:
#             raise ValueTooSmall("Value too small")
        
#         else:
#             raise ValueTooLarge("Value too large")
        
#     except ValueTooSmall as e:
#         print(e)

#     except ValueTooLarge as e:
#         print(e)
    
#     except GuessError as e:
#         print(e)

#     except ValueError:
#         print("You can only enter integers!")

# Task 6



class InvalidName(Exception):
    pass

class InvalidAge(Exception):
    pass

try:
    name=input("Enter the name: ")
    age=int(input("Enter the age: "))

    list1=name.split()

    if name=="":
        raise InvalidName("Name can't be empty")
    elif len(list1)==1:
        raise InvalidName("Name should have 2 words atleast.")
    elif age<18:
        raise InvalidAge("Age must be greater than 18")
    
except InvalidName as e:
    print(e)

except InvalidAge as e:
    print(e)

except ValueError:
    print("Please enter a valid number for age.")
    
else:
    print(f"{name.title()} Congratulation !!! You can vote.")

    


    
