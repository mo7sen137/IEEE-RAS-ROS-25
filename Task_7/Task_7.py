# Problem 1
# For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, 
# multiplication, division and modulus operations.
# The real and imaginary precision part should be correct up to two decimal places.

import math
class Complex:
    def __init__(self, Rnum1, Cnum1, Rnum2, Cnum2):
        self.Rnum1 = Rnum1
        self.Cnum1 = Cnum1
        self.Rnum2 = Rnum2
        self.Cnum2 = Cnum2
        
    def Addition (self):

        R = float (self.Rnum1) + float (self.Rnum2)
        C = float (self.Cnum1) + float (self.Cnum2)

        if C < 0:
            return f"The result of Addition is: {R:.2f}{C:.2f}i"
        elif C > 0:
            return f"The result of Addition is: {R:.2f}+{C:.2f}i"
        else:
            return f"The result of Addition is: {R:.2f}+{C:.2f}i"


    def subtraction (self):
        R = float (self.Rnum1) - float (self.Rnum2)
        C = float (self.Cnum1) - float (self.Cnum2)

        if C < 0:
            return f"The result of subtraction is: {R:.2f}{C:.2f}i"
        elif C > 0:
            return f"The result of subtraction is: {R:.2f}+{C:.2f}i"
        else:
            return f"The result of subtraction is: {R:.2f}+{C:.2f}i"
        

    def multiplication (self):

        R = float( (self.Rnum1*self.Rnum2)-(self.Cnum1*self.Cnum2) )
        C = float( (self.Rnum1*self.Cnum2)+(self.Cnum1*self.Rnum2) )

        if C < 0:
            return f"The result of multiplication is: {R:.2f}{C:.2f}i"
        elif C > 0:
            return f"The result of multiplication is: {R:.2f}+{C:.2f}i"
        else:
            return f"The result of multiplication is: {R:.2f}+{C:.2f}i"
        


    def division (self):

        R = float( (self.Rnum1*self.Rnum2 + self.Cnum1*self.Cnum2)/(self.Rnum2**2 + self.Cnum2**2) )
        C = float( (self.Cnum1*self.Rnum2 - self.Rnum1*self.Cnum2 )/(self.Rnum2**2 + self.Cnum2**2) )

        if C < 0:
            return f"The result of division is: {R:.2f}{C:.2f}i"
        elif C > 0:
            return f"The result of division is: {R:.2f}+{C:.2f}i"
        else:
            return f"The result of division is: {R:.2f}+{C:.2f}i"

class  Mod:
    def __init__(self,Rnum1, Cnum1):
        self.Rnum1 = Rnum1
        self.Cnum1 = Cnum1
        
    def mod(self):
        R = math.sqrt(self.Rnum1**2 + self.Cnum1**2)
        C = 0
        return f"The result of mod is: {R:.2f}+{C:.2f}i"
        
print()
print(Complex(2,1,5,6).Addition())
print()
print(Complex(2,1,5,6).subtraction())
print()
print(Complex(2,1,5,6).multiplication())
print()
print(Complex(2,1,5,6).division())
print()
print(Mod(2,1).mod())
print()
print(Mod(5,6).mod())
print()
print("----------------------------------------------------------------------------------------")


# ------------------------------------------------------------------------------------------------------------------------------
# Problem 2
# You are required to print the angle between the plane made by the points A,B,C and B,C,D in degrees(not radians).Let the angle be phi


import math
class Points:
    def __init__(self,Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz, Dx, Dy, Dz):
        self.Ax = Ax
        self.Ay = Ay
        self.Az = Az
        self.a= [self.Ax, self.Ay, self.Az]

        self.Bx = Bx
        self.By = By
        self.Bz = Bz
        self.b= [self.Bx, self.By, self.Bz]

        self.Cx = Cx
        self.Cy = Cy
        self.Cz = Cz
        self.c= [self.Cx, self.Cy, self.Cz]

        self.Dx = Dx
        self.Dy = Dy
        self.Dz = Dz
        self.d= [self.Dx, self.Dy, self.Dz]

    def Clc (self):
        
        ab = [self.b[0]-self.a[0],
              self.b[1]-self.a[1],
              self.b[2]-self.a[2]
              ]


        bc = [self.c[0]-self.b[0],
              self.c[1]-self.b[1],
              self.c[2]-self.b[2]
              ]


        cd = [self.d[0]-self.c[0],
              self.d[1]-self.c[1],
              self.d[2]-self.c[2]
              ]
        
        X = [ab[1]*bc[2] - ab[2]*bc[1],
            ab[2]*bc[0] - ab[0]*bc[2],
            ab[0]*bc[1] - ab[1]*bc[0]]

        Y = [bc[1]*cd[2] - bc[2]*cd[1],
            bc[2]*cd[0] - bc[0]*cd[2],
            bc[0]*cd[1] - bc[1]*cd[0]]


        dot = (X[0]*Y[0]) + (X[1]*Y[1]) + (X[2]*Y[2])

        mag_X = math.sqrt(X[0]**2 + X[1]**2 + X[2]**2)
        mag_Y = math.sqrt(Y[0]**2 + Y[1]**2 + Y[2]**2)

        co_PHI = dot/(mag_X * mag_Y)
        PHI = math.acos(co_PHI)
        result = round (math.degrees(PHI) , 2)

        
        return f"The angle in radian is: {result}"


print (Points(0, 4, 5, 1, 7, 6, 0, 5, 9, 1, 7, 2).Clc())

print("----------------------------------------------------------------------------------------")
print ()

# ------------------------------------------------------------------------------------------------------------------------------
# Problem 3
# Create a class called BankAccount.


class BankAccount:
    
    def __init__(self, accountNumber, name, balance):

        self.accountNumber = accountNumber
        self.name = name
        self.balance = float(balance)

    def Deposit(self,x):
        self.x = x
        self.balance += self.x
        # print (f"The total: {self.balance}")

    def Withdrawal(self,x):
        self.x = x
        self.balance -= self.x
        # print (f"The total: {self.balance}")


    def bankFees(self):
        fee = 0.05 * self.balance
        self.balance -= fee
        # print (f"The total: {self.balance}")


    def display(self):
        
        print( f"Account Number: {self.accountNumber}\nAccount Name: {self.name}\nAccount Balance: {self.balance} $" )
        

account1 = BankAccount( 2178514584, "Ahmed", 2600)

account1.display()
account1.Deposit(200)
print("-------------------------")
account1.display()
print("-------------------------")
account1.Withdrawal(100)
account1.display()
print("-------------------------")
account1.bankFees()
account1.display()
print()

print("----------------------------------------------------------------------------------------")

# ------------------------------------------------------------------------------------------------------------------------------
# Problem 4
# Write a Python program to create a class representing a  shopping  cart,
# Include methods for adding and removing items, and calculating the total
# price


class ShoppingCart:
    def __init__(self):
        self.items = {}  
    
    def add_item(self, item, price):

        if item in self.items:
            self.items[item] += price
        else:
            self.items[item] = price
    
    def remove_item(self, item, price):

        if item in self.items:
            self.items[item] -= price
        else:
            print(f"{item} is not in the cart. ")
    
    def calculate_total(self):
        return sum(self.items.values())
    
    
    def display_cart(self):
        print("Current Items in Cart:")
        for item, price in self.items.items():
            print(f"{item} --> {price}$")
        print ("----------------------")
        print(f"Total price: {self.calculate_total()}$\n")



cart = ShoppingCart()
cart.add_item("Papaya", 100)
cart.add_item("Papaya", 100)
cart.add_item("Guava", 200)
cart.add_item("Orange", 150)

cart.display_cart()

cart.remove_item("Orange",150)
print("Updated Items in Cart after removing Orange:")

cart.display_cart()

print("----------------------------------------------------------------------------------------")
print ()

# ------------------------------------------------------------------------------------------------------------------------------
# Problem 5
#  Write a Python program to create a class representing a linked list data
#  structure. Include methods for displaying linked list data, inserting and
#  deleting nodes.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete(self, key):
        current = self.head

        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            return

        prev.next = current.next
        current = None


N1 = LinkedList()

for i in [1, 2, 3, 4]:
    N1.insert(i)

print("Initial Linked List:")
N1.display()

print("After insert a new node (4):")
N1.insert(5)
N1.display()

print("After delete a existing node (2):")
N1.delete(2)
N1.display()

print("----------------------------------------------------------------------------------------")
print ()
