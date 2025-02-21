print("2:")

"""
Write a Python program to calculate the area of a trapezoid.
Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5
"""

hight = int(input("Height: "))
base1 = int(input("Base, first value: "))
base2 = int(input("Base, second value: "))

area = 1/2 * hight * (base1 + base2)
print("Output:", area)
