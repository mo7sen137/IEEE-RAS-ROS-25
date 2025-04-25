# Problem 1
# Write a Python program to create a class representing a Circle. 
# Include methods to calculate its area and perimeter.


class circle:
    def __init__(self,radius):
        self.radius= radius

    def  Area_of_circle(self):
        area=3.14*self.radius**2
        
        return f"Area of circle is {area}"
    
    def primeter_of_circle (self):
        perimeter=2*3.14*self.radius
        return f"Perimeter of the circle is {perimeter}"

cir_1 = circle(4)
print(cir_1.Area_of_circle())
print(cir_1.primeter_of_circle())

# -----------------------------------------------------------------------------------------------

# Problem 2
# Write a Python program to create a person class. Include attributes like
# name, country and date of birth. Implement a method to determine the
# person's age.



class Person:
    def __init__(self,Name, Countery, Date_of_birth):
        self.Name = Name
        self.Countery = Countery
        self.Date_of_birth = Date_of_birth
        


    def all(self):
         return f"Name: {self.Name}\nCountery: {self.Countery}\nDate of Birth: {self.Date_of_birth}"
    

    
    def age(self):
        Y,m,d=self.Date_of_birth.split('-')
        Age = 2025 - int(Y)
        return f"Aage: {Age}"

    
person_one = Person("mohsen", "zagazig", "2003-01-15")
print (person_one.all())
print(person_one.age())

# -----------------------------------------------------------------------------------------------

# Problem 3
# Write a Python program to create a calculator class. Include methods for
# basic arithmetic operations.


class calculator:
    def __init__(self,fnum, snum, operation):
        
        self.fnum=fnum
        self.snum=snum
        self.operation=operation

    def clc(self):
        if self.operation == "add":
            total = self.fnum + self.snum
            return f"The Result is: {total}"
        elif self.operation == "sub":
            total = self.fnum - self.snum
            return f"The Result is: {total}"
        elif self.operation == "mul":
            total = self.fnum * self.snum
            return f"The Result is: {total}"
        elif self.operation == "div":
            total = self.fnum / self.snum
            return f"The Result is: {total}"
        else :
            return "What do you want to do with two nums ??"

calc_1=calculator(2, 4, "add")
print(calc_1.clc())

calc_2= calculator(8,6,"sub")
print(calc_2.clc())

# -----------------------------------------------------------------------------------------------

# Problem 4
# Write a Python program to create a class representing a stack data
# structure. Include methods for pushing, popping and displaying elements.

class StackDataStructure:
    stack=[10, 20, 30, 40 ,50]
    
    def __init__(self):
        pass
    def displaying_elements(self):
        return f"The Stack items are: {StackDataStructure().stack}"  
  
    def pushing(self,items):
        self.items=items
        StackDataStructure().stack.append(self.items)
        # print(StackDataStructure().displaying_elements())   if U always want to see the stack after pusshing 
        
    def popping(self):
        StackDataStructure().stack.pop()
        # print(StackDataStructure().displaying_elements())  if U always want to see the stack after popping


one = StackDataStructure()
print(one.displaying_elements())
one.popping()
one.popping()
one.popping()
print(one.displaying_elements())

# -----------------------------------------------------------------------------------------------

# Problem 5
#  Write a Python program to create a class that represents a shape. Include
#  methods to calculate its area and perimeter. Implement subclasses for
#  different shapes like circle, triangle, and square.

from abc import ABCMeta , abstractmethod

class shape(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self,radius):
        self.radius=radius
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass


class circle(shape):
    def __init__(self,radius):
        super().__init__(radius)
    def area(self):
        Area=3.14*self.radius**2
        print(f"Circle Area: {Area}")
    def perimeter(self):
        Perimeter=2*3.14*self.radius
        print(f"Circle Perimeter: {Perimeter}")

class triangle(shape):
    def __init__(self,radius, hight, side1, side2, side3):
        super().__init__(radius)
        self.base=radius
        self.hight=hight
        self.side1=side1
        self.side2=side2
        self.side3=side3
    def area(self):
        cir_Area=0.5*self.base*self.hight
        print(f"triangle Area: {cir_Area}")
    def perimeter(self):
        Perimeter=self.side1 + self.side2 + self.side3
        print(f"triangle Perimeter: {Perimeter}")


class square(shape):
        def __init__(self,radius):
            super().__init__(radius)
            self.length=radius
        def area(self):
            Area=self.length**2
            print(f"Square Area: {Area}")
        def perimeter(self):
            Perimeter=4*self.length
            print(f"Square Perimeter: {Perimeter}")
    
class Rectangle(shape):
        def __init__(self,radius,width):
            super().__init__(radius)
            self.length=radius
            self.width=width
        def area(self):
            Area=self.length * self.width
            print(f"Rectangle Area: {Area}")
        def perimeter(self):
            Perimeter=2*(self.length + self.width)
            print(f"Rectangle Perimeter: {Perimeter}")




circle(7).area()
circle(7).perimeter()
print()
triangle(5, 4, 4, 3, 5 ).area()
triangle(5, 4, 4, 3, 5 ).perimeter()
print()
square(5).area()
square(5).perimeter()
print()
Rectangle(5, 7).area()
Rectangle(5, 7).perimeter()
print()
