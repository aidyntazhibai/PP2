
# 1. Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.

# class Aidynskii:
#     def __init__(self):
#         self.name = ""
#         self.surname = ""
#     def getstring(self):
#         self.name = input("whachuname  ")
#         self.surname = input("whachusurname  ")
#     def bigstring(self):
#         print(self.name.upper(), self.surname.upper())

# mystring = Aidynskii()
# mystring.getstring()

# mystring.bigstring()



# 2. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

# class Shape:
#     def __init__(self):
#         self.length = 0
#     def area(self):
#         return 0
#     def inp(self):
#         self.length = int(input("input the lenght"))


# class Square(Shape):
#     def area(self):
#         print(self.length * self.length)

# f1 = Square()
# f1.inp()
# f1.area()

# 3. Define a class named Rectangle which inherits from Shape class from task 2. 
# Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.



# class Shape:
#     def __init__(self):
#         self.length = 0
#         self.width = 0
#     def area(self):
#         return 0
#     def inp(self):
#         self.length = int(input("input the lenght"))
#         self.width = int(input("input the width"))

# class Square(Shape):
#     def area(self):
#         print(self.length * self.length)

# class Rectangle(Shape):
#     def area(self):
#         print(self.length * self.width)

# f1 = Rectangle()
# f1.inp()
# f1.area()



# ask from teacher later

# class Shape:
#     def __init__(self, lenght, width):
#         self.length = 0
#         self.width = 0
#     def area(self):
#         print(self.length * self.width)


# class Square(Shape):
#     def __init__(self, length):
#         Shape.__init__(self, length)
#     def area(self):
#         print(self.length * self.length)

# class Rectangle(Shape):
#     def __init__(self, length, width):  
#         Shape.__init__(self, length, width)
#     def area(self):
#         Shape.area()



# f1 = Rectangle(3, 4)

# f1.area()


""" 4. Write the definition of a Point class. Objects from this class should have a

        a method show to display the coordinates of the point
        a method move to change these coordinates
        a method dist that computes the distance between 2 points
"""
# without input

# import math

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def show(self):
#         print(f"({self.x}, {self.y})")

#     def move(self, dx, dy):
#         self.x += dx
#         self.y += dy

#     def dist(self, other):
#         return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

# p1 = Point(0, 0)
# p2 = Point(3, 4)



# with input



# import math

# class Point:
#     def __init__(self):
#         self.x = 0
#         self.y = 0

#     def show(self):
#         print(self.x, self.y)

#     def move(self):
#         self.x = self.x + int(input("input how much move in x axis  "))
#         self.y = self.y + int(input("input how much move in y axis  "))
#         print("current pos ", self.x," ",self.y)
 
#     def dist(self):
#         print(math.sqrt((self.x - int(input("second x ")))**2 + (self.y - int(input("second y ")))**2))

#     def inp(self):
#         self.x = int(input("input x"))
#         self.y = int(input("input y"))

# point = Point()
# point.inp()
# point.show()
# point.move()
# point.dist()


# 5. Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. 
# Withdrawals may not exceed the available balance. 
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.



# without input 


# class kaspi:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"{amount} deposited, new balance is {self.balance}")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Withdrawal amount exceeded the current balance")
#         else:
#             self.balance -= amount
#             print(f"{amount} withdrawn, new balance is {self.balance}")

# account = kaspi("Tazhibai Aidyn", 0)

# account.deposit(1000)
# account.withdraw(500) 
# account.withdraw(1500) 


# with input


# class kaspi:
#     def __init__(self):
#         self.owner = ""
#         self.balance = 0
#     def inputowner(self):
#         self.owner = input("input your name")
#         print(self.owner, "your current balance is: ", self.balance )

#     def deposit(self):
#         amount = int(input("input amount you deposit"))
#         self.balance = self.balance + amount
#         print(amount, "deposited, your current balance is: ", self.balance )

#     def withdraw(self):
#         amount = int(input("input amount you want withdraw"))
#         if amount > self.balance:
#             print("Withdrawal amount exceeded the current balance")
#         else:
#             self.balance = self.balance - amount
#             print(amount, "withdrawn, your current balance is: ", self.balance )

# account = kaspi()
# account.inputowner()
# account.deposit()
# account.withdraw() 


# 6. Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define anonymous functions.

# def is_prime(num):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 return False
#         else:
#             return True
#     else:
#         return False

# numbers = [10, 11, 12, 13, 14, 15]
# prime_numbers = list(filter(lambda x: is_prime(x), numbers))
# print(prime_numbers)

