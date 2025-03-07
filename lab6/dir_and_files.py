"""
1. Write a Python program to list only directories, 
files and all directories, files in a specified path. 
"""

import os
path = os.path.expanduser("~/Desktop") #os.listdir(path) получает все файлы и папки в указанной директории.

entries = os.listdir(path)

print("Directories:")
for entry in entries:
    full_path = os.path.join(path, entry)
    if os.path.isdir(full_path):
        print(entry)

print("\nFiles:")
for entry in entries:
    full_path = os.path.join(path, entry)
    if os.path.isfile(full_path):
        print(entry)

print("\nAll Directories and Files:")
for entry in entries:
    full_path = os.path.join(path, entry)
    if os.path.isdir(full_path):
        print(f"[Directory] {entry}")
    else:
        print(f"[File] {entry}")


"""
2. Write a Python program to check for access 
to a specified path. Test the existence, readability, 
writability and executability of the specified path
"""

print("2")

import os

# Путь к файлу well.txt
path = "/Users/tomiriszarylkasyn/Documents/labpp2/labs/lab6/well.txt"

if not os.path.exists(path):
    print("Does not exist")
else:
    if os.access(path, os.R_OK):
        print("Path is readable.")
    else:
        print("Path is not readable.")
    
    if os.access(path, os.W_OK):
        print("Path is writable.")
    else:
        print("Path is not writable.")
    
    if os.access(path, os.X_OK):  #Execute (Исполнение)
        print("Path is executable.")
    else:
        print("Path is not executable.")


"""
3. Write a Python program to test whether a 
given path exists or not. If the path exist 
find the filename and directory portion of the given path. 
"""
print("3")


import os
path = "/Users/tomiriszarylkasyn/Documents/labpp2/labs/lab6"

if os.path.exists(path):
    directory = os.path.dirname(path)
    filename = os.path.basename(path) #os.path.basename(path) берёт последний элемент пути 
    
    print("Path exists at", path)
    print("Directory:", directory)
    print("Filename:", filename)
else:
    print("Path", path, "does not exist")

"""
4. Write a Python program to count the 
number of lines in a text file.
"""

print("4")

import os

def num_counter(path):
    line_count = 0
    with open(path, 'r') as file:
        for line in file:
            line_count += 1
    print("Number of lines in the file:", line_count)
path = "/Users/tomiriszarylkasyn/Documents/labpp2/labs/lab6/well.txt"

if os.path.exists(path): #предотвращает ошибку, если файла нет.
    num_counter(path)
else:
    print("File does not exist at", path)

"""
5. Write a Python program to write a list to a file.
"""

print("5")

mylist = ['apple', 'banana', 'orange']

with open('well.txt', 'w') as file:
    for item in mylist:
        file.write("%s\n" % item)

res = open('well.txt')
print(res.read())


"""
6. Write a Python program to generate 
26 text files named A.txt, B.txt, and so on up to Z.txt
"""

print("6")

import string
import os

folder = "/Users/tomiriszarylkasyn/Documents/labpp2/labs/lab6"
os.makedirs(folder, exist_ok=True)  

for letter in string.ascii_uppercase:
    file_path = os.path.join(folder, letter + ".txt")
    with open(file_path, "w") as f:
        f.write(letter)  # Создаёт и записывает букву
    with open(file_path, "w") as f:
        pass  # Очищает файл

"""
7. Write a Python program to copy 
the contents of a file to another file  
"""

print("7")

with open('/Users/tomiriszarylkasyn/Documents/labpp2/labs/lab6/no.txt', 'r') as my_file_1:
    with open('/Users/tomiriszarylkasyn/Documents/labpp2/labs/lab6/well.txt', 'w') as my_file_2:
        content = my_file_1.read()
        my_file_2.write(content)



"""
8. Write a Python program to delete 
file by specified path. Before deleting 
check for access and whether a given path exists or not.
"""

print("8")

import os

path = "/Users/tomiriszarylkasyn/Documents/labpp2/labs/lab6/no.txt"

if os.path.exists(path):
    os.remove(path)
else:
    print("Path", path, "does not exist!!!")





