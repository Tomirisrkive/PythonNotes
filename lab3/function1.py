#1)A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams
print("1")
def recept(g):
    ounces = g * 28.3495231 
    return ounces

gram=float(input())
sum=recept(gram)
print(sum)

#2)Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)
print("2")
def temperature(f):
    formula = (5/9)*(f-32)
    print(formula)

fah=float(input())
otvet=temperature(fah)



#3)Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):

print("3")

def barlyk(numheads, numlegs):
    r=(numlegs -2*numheads) //2
    s=numheads -r
    return s,r

tauk,koyan=barlyk(35,94)
print(tauk,"tauk")
print(koyan,"koyan")


#4)You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.

print("4")

def isprime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i ==0:
            return False
        return True
    
a=input()
num=[int(n) for n in a.split()]
trueprimes=list(filter(isprime,num)) #проверяет каждое число из списка num с помощью isprime.
print(trueprimes)


#5)Write a function that accepts string from user and print all permutations of that string.

print("5")

from itertools import permutations  # permutations- генерирует все возможные перестановки

def true_permutations(open_str):
    open_list=permutations(open_str)
    for open in open_list:  
        print(''.join(open))

inp=input()
true_permutations(inp)

#6)Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We

print("6")

def strin(n):
    kersinshe=n.split()
    kersinshe.reverse()
    return ' '.join(kersinshe)

a=input()
print(strin(a))


#7)Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

print("7")

def find33(num):
    for i in range(len(num)-1):
        if num[i]==3 and num[i+1]==3:
            return True
    return False

print(find33([1,3,3]))
print(find33([1,3,1,3]))

#8)Write a function that takes in a list of integers and returns True if it contains 007 in order

print("8")


def spy_game(nums):
    for i in range (len(nums)):
        if nums[i]==0:
            for j in range(i,len(nums)-1):
                if nums[j]==0:
                    for k in range(j,len(nums)):
                        if nums[k]==7:
                            return True
                        
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,3,0,6,0,6,7]))
print(spy_game([1,3,5,0,8,0]))

    