print("1")

import datetime

today=datetime.datetime.now()

print(today) #it is together with the time

print(today.date()) #it is no time only date

day1=datetime.date(2025,4,9)
day2=datetime.date(2007,4,9)

diff=day1-day2

print(diff.days)  #difference between day1 and day2

today=datetime.datetime.now()
delta=datetime.timedelta(hours=4,minutes=40)

tog=today+delta
print(tog)

print("2")

import datetime

today=datetime.datetime.now()
print(today.replace(microsecond=0))

print("3")

import re
about="\\d+"
ab=r"\d+"
text="Price:100$,270$"
result=re.findall(about,text)
res=re.findall(ab,text)   #разница нету
print(res)
print(result)

text="MyNameIsTomi"
x = re.sub('([a-z])([A-Z])',r'\1 \2',text)
print(x)






