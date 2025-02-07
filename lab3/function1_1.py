#9)Write a function that computes the volume of a sphere given its radius.

print("9")
def volume(sphere):
    return (4/3)*3.14*(r**3)
r=float(input())
result=volume(r)
print(result)


#10)Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.

print("10")

def removing(n):
    unique = []
    for element in n:
        if element not in unique:
            unique.append(element)
    return unique

a=input()
l=[int(n) for n in a.split()]
r=removing(l)
print(r)

#11)Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam

print("11")


def ispalindrome(s):
    n = len(s)
    for i in range(n // 2):  # Проверяем только половину строки
        if s[i] != s[n - i - 1]:  # Сравниваем символы с начала и конца
            return False
    return True

a = input()
r = ispalindrome(a)
print(r)

#12)Define a functino histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:

print("12")

def histogram(n):
    for i in n:
        print("*"*i)
a=input()
l=[int(n) for n in a.split()]
r=histogram(l)
print(r)

#14)Create a python file and import some of the functions from the above 13 tasks and try to use them.

print("14")

def converter(g):
    ounces = g * 28.3495231
    return ounces

print("Convert grams to ounces:")
gram = float(input("Enter grams: "))
s = converter(gram)
print(gram, "grams is equal to", s, "ounces.")


#13)Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:

print("13")

import random

def guess_number():
    print("Hello! What is your name?")
    player_name = input()
    print(f"Well, {player_name}, I am thinking of a number between 1 and 20.")

    target_number = random.randint(1, 20)
    attempts = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        attempts += 1

        if guess > target_number:
            print("Your guess is too high.")
        elif guess < target_number:
            print("Your guess is too low.")
        else:
            print(f"Good job, {player_name}! You guessed my number in {attempts} guesses!")
            break

guess_number()



