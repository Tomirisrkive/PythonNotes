#findall - Возвращает список, содержащий все совпадени
#search - Возвращает объект Match, если в строке есть совпадение
#split - Возвращает список, в котором строка была разделена при каждом матче
#sub - Заменяет один или несколько совпадений строко
print("1")
import re

#Return every occurrence of "ai":

txt="The rain in Spain,Altain"
x=re.findall("ai",txt)
print(x)

print("2")

#.span()- возвращает кортеш, содержащий начальные и конечные позиции матча.
#.group()- возвращает часть строки, где было совпадение
#.start()- нужен для определение позиции
import re

txt="The rain in Spain Altain"
x=re.search("\s",txt)  #В строке "The rain in Spain Altain" первый пробел находится после слова "The", на позиции 3 (нумерация начинается с 0).

print(x.start())

print("3")

import re

txt="The rain in Spain Altain"
x=re.split("\s",txt)
print(x)

print("4")

txt="The rain in Spain"
x=re.sub("i","9",txt)
print(x)

print("5")

txt="The rain in Spain"
x=re.search(r"\bT\w+",txt)

print(x.group())  #В коде x.group() используется метод .group(), потому что re.search() возвращает объект Match, а метод .group() позволяет получить сам найденный текст.


print("6")



