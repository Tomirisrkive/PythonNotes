#1)Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.

print("1")
class two_classes():
    def getString(self):
        self.name = input()

    def printString(self):
        print(self.name.upper())

b = two_classes()
b.getString()
b.printString()

#2)Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

print("2")

class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()  #базового класса (Shape)
        self.length=length  #Инициализация длины стороны квадрата


    def area(self):
        return self.length*self.length
    
if __name__=="__main__":
    square=Square(int(input()))
    print(square.area())

#3)Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.

print("3")

class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length*self.length

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

sL = float(input())
s = Square(sL)
print(s.area())

rL = float(input())
rW = float(input())
r = Rectangle(rL, rW)
print(r.area())

#4)Write the definition of a Point class. Objects from this class should have a

print("4")
import math

class Point:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def show(self):
        print("Point 1 coordinates: (", self.x1, ",", self.y1, ")")
        print("Point 2 coordinates: (", self.x2, ",", self.y2, ")")

    def move(self, new_x, new_y):
        self.x1 = new_x
        self.y1 = new_y
        print("Moved Point 1 to: (", self.x1, ",", self.y1, ")")

    def dist(self):
        return math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)


x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

p = Point(x1, y1, x2, y2)

# Показываем коорд
p.show()

# Перемещаем первую точку
p.move(5, 7)

# Вычисляем 
distance = p.dist()
print("Distance between points:", distance)

#5)Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

print("5")

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount, "New balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print("Withdrew:", amount, "New balance:", self.balance)


acc = Account("Tomiris", 950)
print(acc.owner)  # Имя Tomiris
print(acc.balance, "tg")  # Баланс 10000

acc.deposit(250)  
acc.withdraw(500)  # Снятие
acc.withdraw(800)  # Снятие, превышающее баланс


#6)Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define anonymous functions

print("6")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = input("Введите через пробел: ").split()
numbers = [int(n) for n in numbers]

# Фильтрация простых чисел
prime_numbers = list(filter(is_prime, numbers))

print(prime_numbers)

