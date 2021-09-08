# форматирование строк 
name='Johon'
age=33

print('My name is ' +name+'. I\'m' + str(age))

print('My name is %(x)s. I\'m %(y)d' %{'x': name, 'y': age}) # второй способ написать 

print('My name is %s. I\'m %s' %(name, age)) # 4 способ написать 

print('Titel: %s, Price: %.2f' %('Sony', 40)) #Titel: Sony, Price: 40.00

print('My name is {} I\'m {}'.format(name, age)) # 5 способ написать 

print('My name is {0} I\'m {1}'.format(name, age)) # 6 способ написать 

print('My name is {x} I\'m {y}'.format(x=name, y=age)) # 7 способ написать 

# f-strings
print(f'My name is {name} I\'m {age}') # 8 способ написать добавили f

print(f'My name is {name} I\'m {age + 5}') # 8 способ написать добавили f можно добавить матиматику

print(f'5 + 2 = {5+2}') # 9 способ написать добавили f

