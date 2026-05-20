# Task 1
# class Point:

#     def __init__(self,x,y):
#         self.x_cod=x
#         self.y_cod=y

#     def __str__(self):
#         return "<{},{}>".format(self.x_cod,self.y_cod)
    
#     def euclidean_distance(self,other):
#         return ((self.x_cod-other.x_cod)**2 + (self.y_cod-other.y_cod)**2)**0.5
    
#     def distance_from_origin(self):
#         return self.euclidean_distance(Point(0,0))
    
# class Line:
#     def __init__(self,A,B,C):
#         self.A=A
#         self.B=B
#         self.C=C

#     def __str__(self):
#         return "{}x+{}y+{}".format(self.A,self.B,self.C)

#     def point_on_line(line,point):
#         if line.A*point.x_cod+line.B*point.y_cod+line.C==0:
#             return "Lies on line"
#         else:
#             return "Does not lie on the line"
        
#     def shortest_distance(line,point):
#         return abs(line.A*point.x_cod+line.B*point.y_cod+line.C)/(line.A**2+line.B**2)**0.5
    
#     def intersect(line,other_line):
#         determinant=(line.A*other_line.B)-(other_line.A*line.B)

#         if determinant==0:
#             return "They are parallel and do not intersect"
#         else:
#             x=((line.B*other_line.C)-(other_line.B*line.C))/determinant
#             y=((line.C*other_line.A)-(other_line.C*line.A))/determinant

#             x=round(x,2)
#             y=round(y,2)

#             return "They will Intersect and the point is:({},{})".format(x,y)
    

# p1=Point(1,1)

# l1=Line(2,3,-6)
# l2=Line(1,-1,-3)

# print(l1.intersect(l2))

# Task 2
# class Car:
#     __instance=0

#     def __init__(self):
#         Car.__instance+=1

#     @staticmethod
#     def getInstanceNo():
#         return Car.__instance
    
# suzuki=Car()
# toyota=Car()
# honda=Car()
# Hyundai=Car()

# print("No of instances: ",Car.getInstanceNo())

# Task 3
# class Rectangle:

#     def __init__(self,length=0,height=0):
#         self.__length=length
#         self.__height=height

#     def setLength(self,len):
#         self.__length=len

#     def setHeight(self,h):
#         self.__height=h

#     def Area(self):
#         return self.__length*self.__height
    
#     def is_square(self):
#       return True if self.__length==self.__height else False
    

# rectangle=Rectangle()
# rectangle.setLength(3)
# rectangle.setHeight(5)

# print(rectangle.Area())
# print(rectangle.is_square())

# Task 4
# from datetime import datetime

# class Product:

#     def __init__(self,name,mfg_date,exp_date):
#         self.name=name
#         self.mfg_date=datetime.strptime(mfg_date,"%Y-%m-%d")
#         self.exp_date=datetime.strptime(exp_date,"%Y-%m-%d")

#     def time_left_for_expiry(self):

#         today=datetime.now()

#         if today>self.exp_date:
#             return "The product has been expired"

#         years=self.exp_date.year-today.year
#         month=self.exp_date.month-today.month
#         day=self.exp_date.day-today.day

#         if day<0:
#             month-=1
#             day+=30
#         elif month<0:
#             years-=1
#             month+=12

#         return f"Time left: {years} Years, {month} Months, and {day} Days."


# p1=Product('milk','2024-5-20','2026-9-11')
# print(p1.time_left_for_expiry())

# Task 5

# class Student:

#     def __init__(self):
#         self.__id=None
#         self.__age=None
#         self.__marks=None

#     def set_id(self,id):
#         self.__id=id

#     def set_age(self,age):
#         self.__age=age

#     def set_marks(self,marks):
#         self.__marks=marks

#     def __validate_marks(self):
#         return 0<= self.__marks <=100
    
#     def __validate_age(self):
#         return self.__age>20
    
#     def check_qualification(self):
#         if self.__validate_marks() and self.__validate_age():
#             return self.__marks>=65
#         else:
#             return False
        
# s1=Student()
# s1.set_id(1)
# s1.set_age(21)
# s1.set_marks(64)

# print(s1.check_qualification())

# Task 6 & 7
class Scoop:
    __no_of_scoops=0
    def __init__(self,flavor,no_of_scoop=1):
        self.flavor=flavor
        self.no_of_scoop=no_of_scoop
        self.__price=None
        Scoop.__no_of_scoops+=1

    def __str__(self):
        return "Flavor - {}, No of Scoop -{}, Price - {}".format(self.flavor,self.no_of_scoop,self.get_price())

    def set_price(self,price):
        self.__price=price

    def get_price(self):
        return self.__price

    @staticmethod
    def sold():
        print("{} scoops sold".format(Scoop.__no_of_scoops))

class Bowl:
    __no_of_bowls=0
    def __init__(self,max_scoops=3):
        self.__scoop_list=[]
        self.max_scoops=max_scoops
        Bowl.__no_of_bowls+=1
    
    def __str__(self):
        result=""
        for items in self.__scoop_list:
            result+=items.flavor+"\n"

        return result.strip()
        

    def add_scoops(self,*scoop:Scoop):
        for item in scoop:

            current_scoops=0
            for existing_items in self.__scoop_list:
                current_scoops+=existing_items.no_of_scoop

            if current_scoops+item.no_of_scoop<=self.max_scoops:
                self.__scoop_list.append(item)
                print("{} added".format(item.flavor))
            else:
                print("{} not added. Bowl is full".format(item.flavor))

        
    def display(self):
        bowl_price=0
        print("Displaying Bowl {}...".format(self.__no_of_bowls))
        for item in self.__scoop_list:
            print(item)
            bowl_price+=item.get_price()*item.no_of_scoop
        
        print("Price of bowl",bowl_price)

    @staticmethod
    def sold():
        print("{} bowls sold".format(Bowl.__no_of_bowls))

choco = Scoop('chocolate', 1)
choco.set_price(100)
print(choco)


berry = Scoop('berry', 2)
berry.set_price(120)
print(berry)

vanilla = Scoop('vanilla') 
vanilla.set_price(150)
print(vanilla)
print()
print()

bowl1 = Bowl() 
bowl1.add_scoops(choco) 
bowl1.add_scoops(berry, vanilla) 
bowl1.display()
print()
print()

bowl2 = Bowl(2)
bowl2.add_scoops(berry)
bowl2.add_scoops(choco)

bowl2.display()
Bowl.sold()


# choco = Scoop('chocolate')
# print(choco)
# choco.set_price(100)
# berry = Scoop('berry')
# berry.set_price(120)
# print(berry)
# vanilla = Scoop('vanilla')
# vanilla.set_price(150)

# bowl = Bowl()

# bowl.add_scoops(choco) 
# bowl.add_scoops(berry, vanilla) # 

# print(bowl)

# bowl.display()

# Scoop.sold()
# Bowl.sold()

