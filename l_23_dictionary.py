# Неупорядочная коллекция элементов, множества элементов с доступом к элементам по ключу и значению 
# ассоциация по ключу и значению цена, название, тип..
# асоциативными масивами, хеш таблица, 

d = {} # <class 'dict'>
product1 = {'title': 'Sony', 'price': 1000} #способы создания словарей 
product2 = dict(title='iphone', price=110) # кавычки не нужны 
product3 = dict.fromkeys (['price1','price2', 'price3'], 50) # создать словарь с одинаковым значением для всех елементов 
# print(product3) #{'price1': 50, 'price2': 50, 'price3': 50}

users = [ #{'ata@gmail.com': 'ata', 'kety@gmail.com': 'kety', 'john@gmail.com': 'john'}
    ['ata@gmail.com', 'ata'],  # красивая запись длясоздания словаря
    ['kety@gmail.com', 'kety'],
    ['john@gmail.com', 'john']
]
d_users =dict(users)
# print(d_users)
# print(d)
# print(product1)
print(product2)

nums = {i: i+1 for i in range (1,10)} #  генератор для создания словарей 
# print (nums) #{1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10}

# print(product1['title']) #Sony простой способ получения значений из словаря 
# print(product1['price']) #1000
# print(nums[1])
# print(product1.get('title', 'no')) # можно вбивать не существующие элементы без вывода ошибок


for key in product1:
    # print(product1[key])
    print(f'{key}: {product1[key]}')    # title: Sony
                                        # price: 1000
# print (product1.items()) # dict_items([('title', 'Sony'), ('price', 1000)])
for key, Value in product1.items() : # данный метод возвращает пары ключ значение
    print(key, Value) # выводит тоже самое значение 

  