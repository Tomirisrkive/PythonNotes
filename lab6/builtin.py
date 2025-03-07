"""
1. Write a Python program with builtin function to multiply all the numbers in a list
"""

from functools import reduce

def multiplying(n):
    return reduce(lambda x, y: x*y, n)



liist=[12,3,4,5,6,7,8,9,10]
res=multiplying(liist)
print(res)

"""Write a Python program with builtin function that accepts a string a"""

print("2")

message = 'HEllo, World, how are you?'

cnt_upper = 0
cnt_lower = 0

for letter in message: 
    if ord(letter) >= 65 and ord(letter) <= 90:
        cnt_upper += 1
    elif ord(letter) >= 97 and ord(letter) <= 122: 
        cnt_lower += 1

print("Uppercase letters:", cnt_upper)
print("Lowercase letters:", cnt_lower)

print("3")

"""
3. Write a Python program with builtin function that checks whether a passed string is palindrome or not.
"""
#madam- Yes

def ispalindrome(s):
    if s==''.join(reversed(s)):
        return "YES"
    else:
        return "NO"



s=input()
res=ispalindrome(s)
print(res)

print("4")

"""
4. Write a Python program that invoke square root function after specific milliseconds. 
    ```
    Sample Input:
    25100
    2123
    Sample Output:
    Square root of 25100 after 2123 miliseconds is 158.42979517754858
    ````
"""


import time
import math

n = int(input())
milisec = int(input())

time.sleep(milisec / 1000.0)
x = math.sqrt(n)

print("Square root of", n, "after", milisec, "milliseconds is", x)

print("5")

"""
5. Write a Python program with builtin function that returns True if all elements of the tuple are true.
"""

def tuptrue(mine):
    if all(mine):
        return True
    else:
        return False

mytuple=(1,2,3,4,5,6,7,8,9,10)
print(tuptrue(mytuple))

