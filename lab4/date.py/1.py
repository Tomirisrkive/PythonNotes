#subtract five days from current date.
print("1st exercise:")

import datetime

tday=datetime.datetime.now()
tdelta=datetime.timedelta(days=5)

print(tday-tdelta)


print()
#print yesterday, today, tomorrow.
print("2nd exercise:")

import datetime

tday=datetime.datetime.today()
print("Today:", tday)


yest=tday-datetime.timedelta(days=1)
print("Yesterday:", yest)


tmrw=tday+datetime.timedelta(days=1)
print("Tomorrow:", tmrw)

print()

#drop microseconds from datetime.
print("3rd exercise:")

import datetime

tday=datetime.datetime.now()
print(tday.replace(microsecond=0))



print()
#calculate two date difference in seconds.
print("4th exercise:")

import datetime

def difference(first, second):
    well=first-second
    return well.total_seconds()

date1 = datetime.datetime.now()
date2 = datetime.datetime.now()-datetime.timedelta(days=2)

res = difference(date1, date2)
print("Difference in seconds:", res)