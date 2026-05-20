# Task 1

# class Vehicle:
#     def __init__(self,seating_capacity):
#         self.seating_capacity=seating_capacity

#     def fare(self):
#         return self.seating_capacity*100
    
# class Bus(Vehicle):
#     def __init__(self, seating_capacity):
#         super().__init__(seating_capacity)

#     def fare(self):
#         return super().fare()+super().fare()*0.1
    

# bus=Bus(50)

# Task 2
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#     def __str__(self):
#         return "{},{}".format(self.x,self.y)
    

# class Location:
#     def __init__(self,current_loc,dest_loc):
#         self.current_location=current_loc
#         self.destinition_location=dest_loc

#     def reflection(self):

#         x_cod=self.destinition_location.x
#         y_cod=-self.destinition_location.y

#         print("{},{}".format(x_cod,y_cod))

# start=Point(2,5)
# end=Point(8,4)

# my_location=Location(start,end)
# my_location.reflection()

        
# Task 3
# from abc import ABC,abstractmethod

# class Polygon(ABC):

#     @abstractmethod
#     def get_area(self):
#         pass

# class Rectangle(Polygon):

#     def __init__(self,length,width):
#         self.length=length
#         self.width=width

#     def get_area(self):
#         return self.length*self.width
    
# class Triangle(Polygon):
#     def __init__(self,base,height):
#         self.base=base
#         self.height=height

#     def get_area(self):
#         return 0.5*self.base*self.height
        
# t1=Triangle(2,5)
# print(t1.get_area())

# r1=Rectangle(2,5)
# print(r1.get_area())

# Task 4
# class Bill:
#     def __init__(self,amount):
#         self.amount=amount

# class CashPayment(Bill):
#     def process_payment(self):
#         print( "Paying {} through cash payment".format(self.amount))
    
# class ChequePayment(Bill):
#     def __init__(self, amount,check_number,bank_name):
#         super().__init__(amount)
#         self.check_number=check_number
#         self.back_name=bank_name

#     def process_payment(self):
#         print( "paying through check no: {}, bank_name: {}, amount: {}".format(self.check_number,self.back_name,self.amount))
        

# print("--- Transaction 1 ---")

# grocery_bill = CashPayment(500)
# grocery_bill.process_payment()

# print("\n--- Transaction 2 ---")

# rent_bill = ChequePayment(15000, "CHK987654", "Habib Bank")
# rent_bill.process_payment()

# Task 5
class FlexibleDict(dict):

    def __getitem__(self, key):
        
        
        if key in self:
            return super().__getitem__(key)
            
       
        if type(key) == str and key.isdigit():
            key1 = int(key)
            if key1 in self:
                return super().__getitem__(key1)
                
        
        if type(key) == int:
            key2 = str(key)
            if key2 in self:
                return super().__getitem__(key2)
                
       
        raise KeyError(key)
    
    

fd = FlexibleDict()
fd['a'] = 100
print(fd['a']) 

fd[5] = 500
print(fd[5]) 

fd[3] = 100
print(fd['3']) 

fd['1'] = 200
print(fd[1]) 

