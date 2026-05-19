# Task 1
# class Rectangle:


#     def __init__(self,length,width):
#         self.length=length
#         self.width=width

#     def calc_perimeter(self):
#         return 2*(self.length+self.width)
        

#     def calc_area(self):
#         return self.length*self.width
       

#     def display(self):
#         print("The length of rectange is: ",self.length)
#         print("The width of rectangle is: ",self.width)
#         print("The perimeter of rectangle is: ",self.calc_perimeter())
#         print("The area of rectangle is: ",self.calc_area())

# rectangle=Rectangle(3,4)
# rectangle.display()

# Task 2
# class BankAccount:

#     def __init__(self,accNo:int,name:str,balance:int):
#         self.accNo=accNo
#         self.name=name
#         self.balance=balance

#     def Deposit(self,amount:int):
#         self.balance+=amount
#         print("Deposited amount of: {}".format(amount))

#     def Withdraw(self,amount:int):
#         if amount<=self.balance:
#             self.balance-=amount
#             print("{} has been withdrawn".format(amount))
#         else:
#             print("Not sufficant amount!")

#     def Bank_Fees(self):
#         bank_fees=(self.balance*5)/100
        
#         self.balance-=bank_fees
#         print("{} has been deducted due to bank fees".format(bank_fees))
    
#     def display(self):
#         print("Account no:",self.accNo)
#         print("Account name: ",self.name)
#         print("Account balance: ",self.balance)


# newAccount=BankAccount(213456723,"Wahab",10000)

# newAccount.Bank_Fees()
# newAccount.Deposit(10000)
# newAccount.Withdraw(4320)

# newAccount.display()

# Task 3
# class Computation:
#     def __init__(self):
#         pass

#     def Factorial(self,n):
#         product=1
#         for i in range(1,n+1):
#             product*=i

#         return product
    
#     def naturalSum(self,n):
#         sum=0
#         for i in range(1,n+1):
#             sum+=i

#         return sum
    
#     def testPrime(self,n):
#         if n==1:
#             return 'Not Prime'
#         else:
#             for i in range(2,n):
#                 if n%i==0:
#                     return 'Not Prime'
                    
                
#         return 'Prime'
    
#     def testPrims(self, num1, num2):

#         smaller = min(num1, num2) 
        
     
#         for i in range(2, smaller + 1):
            
#             if num1 % i == 0 and num2 % i == 0:
     
#                 return f"{num1} and {num2} are Not Coprime"
                

#         return f"{num1} and {num2} are Coprime"
    
#     def tableMult(self,n):
#         for i in range(1,11):
#             print(f'{n}*{i}={n*i}')

#     def allTablesMult(self):
#         for i in range(1,10):
#             for j in range(1,11):
#                 print(f'{i}*{j}={i*j}')

#             print()

#     @staticmethod
#     def listDiv(n):
#         list1=[]
#         for i in range(1,n+1):
#             if n%i==0:
#                 list1.append(i)

#         return list1
    
#     def listDivPrime(self,n):
#         primeDiv=[]
#         list1=Computation.listDiv(n)
#         for item in list1:
#             if self.testPrime(item)=='Prime':
#                 primeDiv.append(item)

#         return primeDiv



# Calculator=Computation()
# print(Calculator.listDiv(150))
# print(Calculator.listDivPrime(150))

# Task 4
# import random
# class FlashCards:
#     def __init__(self):

#         self.fruits = {
#             "Banana": "yellow",
#             "Strawberries": "pink",
#             "watermelon": "green",
#             "apple": "red",
#             "orange": "orange"
#         }

#     def quiz(self):

#         while True:
#             print('WELCOME TO FRUIT QUIZ')
#             fruit_list=list(self.fruits.keys())
#             fruit=random.choice(fruit_list)

#             color=self.fruits[fruit]

#             print(f"What is the color of {fruit}?")
#             user_input=input()

#             if user_input.lower()==color.lower():
#                 print("Amazing!")
#             else:
#                 print("You are wrong fool!")

#             check=input("Enter 0, if you want to play again:")

#             if check!='0':
#                 break

# game=FlashCards()

# game.quiz()

# Task 5
class Instructor:

    def __init__(self):
        self.__name=""
        self.__experience=0
        self.__feedback=0
        self.__technology_skills=[]

    def setName(self,name:str):
        self.__name=name

    def setExperience(self,exp:float):
        self.__experience=exp
    
    def setFeedback(self,fb:float):
        self.__feedback=fb

    def setTechnologySkills(self,ts:list):
        self.__technology_skills=ts

    def check_eligibility(self):
        if self.__experience>3 and self.__feedback>=4.5:
            return True
        elif self.__experience<=3 and self.__feedback>=4:
            return True
        
        return False
    
    def allocate_course(self,technology):

        if self.check_eligibility()==True and technology in self.__technology_skills:
            return True
        
        return False
    

my_instructor=Instructor()

instructor_1 = Instructor()
instructor_1.setName("Wahab")
instructor_1.setExperience(5)
instructor_1.setFeedback(4.8)
instructor_1.setTechnologySkills(["Python", "Java", "C++"])

print(f"Testing {instructor_1._Instructor__name} (Exp: 5, FB: 4.8, Skill: Python):")

print("Eligible?", instructor_1.check_eligibility()) 
print("Allocated Python?", instructor_1.allocate_course("Python"))
print("-" * 30)



instructor_2 = Instructor()
instructor_2.setName("Ali")
instructor_2.setExperience(2)
instructor_2.setFeedback(4.2)
instructor_2.setTechnologySkills(["HTML", "CSS"])

print(f"Testing {instructor_2._Instructor__name} (Exp: 2, FB: 4.2, Skill: HTML/CSS):")

print("Eligible?", instructor_2.check_eligibility()) 
print("Allocated Python?", instructor_2.allocate_course("Python"))
print("-" * 30)



instructor_3 = Instructor()
instructor_3.setName("Sara")
instructor_3.setExperience(6)
instructor_3.setFeedback(4.1) 
instructor_3.setTechnologySkills(["Python", "Data Science"])

print(f"Testing {instructor_3._Instructor__name} (Exp: 6, FB: 4.1, Skill: Python):")

print("Eligible?", instructor_3.check_eligibility()) 
print("Allocated Python?", instructor_3.allocate_course("Python"))
print("-" * 30)

