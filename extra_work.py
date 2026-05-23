from dataclasses import dataclass

@dataclass
class Person:
    name:str
    age:int

p1=Person('Wahab Ali',21)
p2=Person('Wahab Ali',21)
print(p1,p2)
print(p1==p2)
