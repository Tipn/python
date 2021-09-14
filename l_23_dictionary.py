# Неупорядочная коллекция элементов, множества элементов с доступом к элементам по ключу и значению 
# ассоциация по ключу и значению цена, название, тип..
# асоциативными масивами, хеш таблица, 

d = {} # <class 'dict'>
product1 = {'title': 'Sony', 'price': 1000} #способы создания словарей 
product2 = dict(title='iphone', price=110) # кавычки не нужны 

users = [ #{'ata@gmail.com': 'ata', 'kety@gmail.com': 'kety', 'john@gmail.com': 'john'}
    ['ata@gmail.com', 'ata'],  # красивая запись длясоздания словаря
    ['kety@gmail.com', 'kety'],
    ['john@gmail.com', 'john']
]
d_users =dict(users)
print(d_users)
print(d)
print(product1)
print(product2)