# datetime
from datetime import date, datetime
"""
# date
today = date.today()
print(today) #2021-09-30
print(today.day) #30
print(today.month) #9
print(today.year) #2021
print(today.weekday()) #3
"""
datetime
now = datetime.now()
now2 = datetime.today()
"""
print(now, now2, sep='\n')
print(now) #2021-09-30 16:37:46.612994
print(now.day) #30
print(now.month) #9
print(now.year) #2021
print(now.hour) #16
print(now.minute) #45
print(now.second) #50

days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
print(days[now.weekday()]) # чт
"""

strftime