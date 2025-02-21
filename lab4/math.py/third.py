
print("3:")
"""
Write a Python program to calculate the area of regular polygon.
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
"""


import math
num = int(input("Input number of sides: "))
lenth = int(input("Input the length of a side: "))

area = int(num * pow(lenth, 2) / math.tan((math.pi) / num) / 4)
print("The area of the polygon is:", area)
