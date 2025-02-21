"""
 Create a generator that generates the squares
 of numbers up to some number N.
"""

def generator(n):
    for x in range(1, 1+n):
        yield x**2

N=int(input("give value to N: "))
func=generator(N)

for y in func:
    print(y)

"""
Write a program using generator to print 
the even numbers between 0 and n in comma separated 
form where n is input from console.
"""
print("2nd exercise:")

def generator(n):
    for x in range(1, 1+n):
        if x%2==0:
            yield x

n=int(input("give value to N: "))
well=', '.join(str(i) for i in generator(n))
print(well)

# func=generator(n)

# for y in func:
#     print(y)



"""
Define a function with a generator 
which can iterate the numbers, which are 
divisible by 3 and 4, between a given range 0 and n.
"""
print("3rd exercise:")
def generator(n):
    for x in range(1, 1+n):
        if x%3==0 and x%4==0:
            yield x

n=int(input("give value to N: "))
well=', '.join(str(i) for i in generator(n))
print(well)

# func=generator(n)

# for y in func:
#     print(y)


"""
Implement a generator called squares 
to yield the square of all numbers from (a) to (b). 
Test it with a "for" loop and print each 
of the yielded values.
"""
print("4th exercise:")

def squares(a, b):
    for x in range(a,b+1):
            yield x**2
a=int(input("give value a: "))
b=int(input("give value for b: "))
well=', '.join(str(i) for i in squares(a, b))
print(well)

# func=squares(a, b)

# for y in func:
#     print(y)



"""
Implement a generator that returns 
all numbers from (n) down to 0.
"""
print("5th exercise:")

def down(n):
    for x in range(n, -1, -1):
        yield x

N=int(input("give value to N: "))
well=', '.join(str(i) for i in down(n))
print(well)

# func=down(N)

# for y in func:
#     print(y)