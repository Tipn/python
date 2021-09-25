print('таблица умножения') 

for x  in range(1, 10):
    for y in range(2, 10):
        print (f'{x} * {y} = {x*y}\t', end='')
    print(' ')
else:
    print('Well done')
#____________________

time1 = 3 #--> liters +1
time2 = 6.7 #--> liters =3
time3 = 11.8 #--> liters =5
def p():
    print (time3//2)
p()
print (time1//2)
print (time2//2)
print (int(time3//2)) # вернет без нуля
#_____________________

s= 'hello world'
if ' ' in s:
    s=s.upper()
    # print(s.capitalize())
else:
    s = s.lower()
print (s)
# answer
def set_register(s):
    if ' ' in s:
        return s.upper()
    else:
        return s.lower()
print(set_register('hello world'))
print(set_register('hello,world'))


