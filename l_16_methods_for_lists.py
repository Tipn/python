#методы для работы со списками 

l = [1, 2, 3, 'hello', ['test', 10], 'word', True] 
name = ['Ivanov', 'petrov', 'sidorov']

print(name[0]) # получу значение из переменной name первое
print(l[4][1]) # список из списка
print(l[0:4])  # вывести все до 4 элемента 

l[1] = 'world!'  # 1, 'world!', 3, 'hello', ['test', 10], 'word', True]
l[0:2] = [10,15] # [10, 15, 3, 'hello', ['test', 10], 'word', True]

l.append('new') # добавление в список : [10, 15, 3, 'hello', ['test', 10], 'word', True, 'new']
l.extend([5,7])
l2 = ['hi',19] #добавление списков дополнительными вариантами : [10, 15, 3, 'hello', ['test', 10], 'word', True, 'new', 5, 7, 'hi', 19]
l= l+l2
l.insert(1, 'test')  # вставляет на i-ый элемент значение х : [10, 15, 3, 'hello', ['test', 10], 'word', True, 'new', 5, 7, 'hi', 19]
l.remove('word') # удаляет елемент : [10, 'test', 15, 3, 'hello', ['test', 10], True, 'new', 5, 7, 'hi', 19]
#l=l.pop ([1]) # удаляет i-ый элемент и возвращает его. Если индек не указан, удаляется последний элемент :
# возвращает положение первого элемента сд значением х при этом поиск ведется от start до end 
l3 = ['hello', 'hi', 'Pavel', 'kut', 'test']
l3.sort()
print (', '.count('test'), 13, sep='\n')

print(l3)