# if оператор http://pythonicway.com/python-operators
# True
# False

# == #

# print (2 > 3) # False
# print (2 < 3) # True
# print (3 == 3) # True

# print (3 == 3) # True
'''
if выражение1:
    блок кода1
elif выражение 2:
    блок кода 2
else:
    блок кода 3
'''

# x = 0
# if x :
#     print ('переменная х вернула ИСТИНУ')

# else:
#     print ('Переменная х вернула ЛОЖЬ')

# light ='red'

# if light == 'red':
#     print ('stop')
# elif light ==('yellow'):
#     print ('wait')
# elif light ==('green'):
#     print ('Go!')
# else:
# #     print ('What?')

# age = int(input('сколько вам лет?'))
# x = 18 - age
# if age >=18:
#     prnt('Добро пожаловать')
# else:
#     print (f'Вам {age}, вам осталось {18-age} лет')
    
time = 11
if time < 12 or time > 13 :  # любое условие должно вернуть тру и будет тру ИЛИ
    print ('Open')
else:
    print('Close') 

time = 12
day = 'st'

if time >= 8 and day != 'su' :  # каждое условие должно вернуть тру и будет тру И
    print ('Open')
else:
    print('Close') 


x=0
if not x:
    print ('ok')
else:
    print('NO')



x = 1

res = 'OK' if x else 'NO'
print (res)
