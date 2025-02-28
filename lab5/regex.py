import re

with open('/Users/tomiriszarylkasyn/Documents/labpp2/labs/lab5/test.txt','r') as my_file:
    my_text = my_file.read()


"""
1. Write a Python program that matches 
a string that has an `'a'` followed by 
zero or more `'b'`'s.
"""

x = re.search('ab*',my_text)
print(x)

"""
2. Write a Python program that matches 
a string that has an `'a'` followed by 
two to three `'b'`.
"""

y = re.search('ab{2,3}',my_text)
print(y)


"""
3. Write a Python program to 
find sequences of lowercase letters 
joined with a underscore.
"""

print(re.findall('[a-z+_]',my_text))


"""
4. Write a Python program to find 
the sequences of one upper case letter 
followed by lower case letters.
"""

print(re.findall('[A-Z][a-z]+',my_text))


"""
5. Write a Python program that matches 
a string that has an `'a'` followed by 
anything, ending in `'b'`.
"""

print(re.findall('a.*b',my_text))


"""
6. Write a Python program to replace 
all occurrences of space, comma, or 
dot with a colon.
"""

my_text = "Hi. what is your name, my name is Tomiris"

def change(match): # 'change()' changes our match with colon
    return ":"

x = re.sub('[.,\s]', change, my_text) # finding characters that are either a dot, comma or a whitespace and whenever it's found -> call the function 'change'
print(x)


"""
7. Write a python program to 
convert snake case string to 
camel case string.
"""

import re

my_text = 'some_sample_data'

def to_camel_case(match):
    return match.group(1).upper()

x = re.sub('_([a-z])', to_camel_case, my_text) # we write ([a-z]) to get only the inner group, which is our letter after an underscore '_' 
print(x) 


"""
8. Write a Python program 
to split a string at uppercase letters.
"""


my_text = 'My Name Is Tomiris'
x = re.split(r'(?=[A-Z])', my_text)
print(x[1:])


"""
9. Write a Python program to 
insert spaces between words 
starting with capital letters.
"""

my_text = 'HereIsSomeData'

x = re.sub('([a-z])([A-Z])', r'\1 \2', my_text) # first match: 'eI' ----> \1 -> 'e', \2 -> 'I'
                                                # second match: 'sS' ----> \1 -> 's', \2 -> 'S'
                                                # third match: 'eD' ----> \1 -> 'e', \2 -> 'D'      
print(x)




"""
10. Write a Python program to 
convert a given camel case string to snake case.
"""
import re  

my_text = 'convertThisExampleText'

def change(match):
    return match.group(1) + '_' + match.group(2).lower()

x = re.sub(r'([a-z])([A-Z])', change, my_text)

print(x)


"""
1. 'eI' → 'e' + '_' + 'i' → 'here_isSomeData'
2. 'sS' → 's' + '_' + 's' → 'here_is_someData'
3. 'eD' → 'e' + '_' + 'd' → 'here_is_some_data'

"""

