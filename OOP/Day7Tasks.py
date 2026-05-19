class Rectangle():


    def __init__(self,length,width):
        self.length=length
        self.width=width

    def calc_perimeter(self):
        return 2*(self.length+self.width)
        

    def calc_area(self):
        return self.length*self.width
       

    def display(self):
        print("The length of rectange is: ",self.length)
        print("The width of rectangle is: ",self.width)
        print("The perimeter of rectangle is: ",self.calc_perimeter())
        print("The area of rectangle is: ",self.calc_area())

rectangle=Rectangle(3,4)
rectangle.display()