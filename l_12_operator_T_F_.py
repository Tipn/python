# if оператор http://pythonicway.com/python-operators
# True
# False

# == # оператор сравнения проверяется значение 
# 

# print (2 > 3) # False
# print (2 < 3) # True
# print (3 == 3) # True

# print (3 == 3) # True
'''
if выражение1: вырожение в котором можно записать условие которое вернет T или F  
    блок кода1
elif выражение 2: - ElseIf иначе если 
    блок кода 2
else:
    блок кода 3 - иначе 
'''

x = 0 
if x :    # строка не верна,х равен 0 . значит будет выполнятся второе условие 
    print ('переменная х вернула ИСТИНУ')
else:
    print ('Переменная х вернула ЛОЖЬ')

if 1 :    # строка верна, 1 не задано ни одного другого значения. значит будет выполнятся первое условие 
    print ('переменная х вернула ИСТИНУ')
else:
    print ('Переменная х вернула ЛОЖЬ')


# light ='red'

# if light == 'red':            # если пременная свет = красный
#     print ('stop')            # напечатай стоп
# elif light ==('yellow'):      # иначе если свет = желтый 
#     print ('wait')            # напечатай жди
# elif light ==('green'):       #
#     print ('Go!')             #
# else:                         #
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
