import time

localtime=time.localtime(time.time())
print("Local time is:",localtime)

localtime=time.asctime(time.localtime(time.time()))
print("Localtime is:",localtime)


import calendar

cal=calendar.month(2019,3)
print("Here is the calenar:")
print(cal)