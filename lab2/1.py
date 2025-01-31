#1) Boolean Values
print(10>9)
print(10==9)
print(10<9)

#2)Python Operators
print(19+5)
print(20*5)

#3)Python Lists
myword=["one ","two","three"]
print(myword)
print(len(myword))

#4)Access List Items
myword=["one ","two","three"]
print(myword[1])
print(myword[0])

#5)Change List Items
myword=["one ","two","three"]
myword[2]="five"
print(myword)

#6)Add List Items
myword=["one ","two","three"]
myword.append("nine")
print(myword)

#7)Remove Specified Item
myword= ["apple", "banana", "cherry", "banana", "kiwi"]
myword.remove("apple")
print(myword)

#8)Loop Through a List
myword= ["apple", "banana", "cherry"]
for i in range(len(myword)):
  print(myword[i])

#9)List Comprehension
myword= ["apple", "banana", "cherry"]
newword=[]

for n in myword:
  if "a" in n:
    newword.append(n)

print(newword)

#10)Sort Lists
mydigit= [100, 50, 65, 82, 23]
mydigit.sort()
print(mydigit)

#11)Copy Lists
myword=["one","two","three","five"]
newl=myword.copy()
print(newl)

#12)Two lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#13)Python Turples
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

myword=("apple")
print(type(myword))

myword = ("apple", "banana", "cherry")
print(type(myword))

#14)Access Turple (кортеж)
myword = ("apple", "banana", "cherry")
print(myword[-1])

myword = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(myword[1:4])

myword = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(myword[2:])

myword = ("apple", "banana", "cherry")
if "cherry" in myword:
  print("Of course, 'cherry' is in the fruits tuple")


#15)Update Turples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

myword = ("apple", "banana", "cherry")
y = ("orange",)
myword += y

print(myword)

#16)Unpacking a Tuole
fruits = ("apple", "banana", "cherry","doll","kiwi")

(green, yellow, pink,red,green) = fruits

print(green)
print(yellow)
print(pink)
print(red)
print(green)


#17)Loop Tuples
mydigit= ("apple", "banana", "cherry")
for x in mydigit:
  print(x)


#18)Join Tuples
tuple1 = ("A", "B" , "C")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#19)Python Sets
myset = {"apple", "banana", "cherry", "apple"}

print(myset)

#20)Access Set Items
myset = {"apple", "banana", "cherry"}
print("cherry" not in myset)

#21)Add Set Items
myset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

myset.update(tropical)
print(myset)

#22)Remove Set Items
myset = {"apple", "banana", "cherry"}
myset.remove("banana")
print(myset)

#23)Loop Sets
myset = {"apple", "banana", "cherry"}
for x in myset:
  print(x)

#24)Join Sets
set1 = {"A", "B", "C", "D", "F", "G"}
set2 = {1, 2, 3, 4, 5, 6}
set3 = set1.union(set2)
print(set3)

#25)Dictionaries
mydict = {
  "brand": "Ferrary",
  "model": "Hamilgton",
  "year": 1985
}
print(mydict)

#26)Accessing Items
mydict = {
  "brand": "Ferrary",
  "model": "Hamilgton",
  "year": 1985
}
x= mydict.get("model")
print(x)

#Change Dictionary Items
mydict = {
  "brand": "Ferrary",
  "model": "Hamilgton",
  "year": 1985
}
mydict["year"]=2025
print(mydict)

#Add
mydict = {
  "brand": "Ferrary",
  "model": "Hamilgton",
  "year": 1985
}
mydict["color"]="red"
print(mydict)

#Remove
mydict = {
  "brand": "Ferrary",
  "model": "Hamilgton",
  "year": 1985
}
mydict.pop("model")
print(mydict)

#Dictionaries
x = {'type' : 'fruit', 'name' : 'apple'}
for y in x.values():
  print(y)

#Copy
mydict = {
  "brand": "Ferrary",
  "model": "Hamilgton",
  "year": 1985
}
youdict=mydict.copy()
print(youdict)

#Nested
a = {'name' : 'John', 'age' : '20'}
b = {'name' : 'May', 'age' : '23'}
customers = {'c1' : a, 'c2' : b}
print(customers['c2']['name'])


#27)If..Else
a = 100
b = 250
if b > a:
  print("b is greater than a")


#28)While Loops
i = 2
while i < 9:
  print(i)
  if i == 3:
    break
  i += 1

#29)For Loops
fruits = ["apple", "banana", "cherry","kiwi"]
for x in fruits:
  if x == "cherry":
    break
  print(x)
