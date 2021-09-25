# s = 'Hello world'
# if ' ' in s:
#     s = s.upper()
# else:
#     s = s.lower()
# print(s)

# s2 = 'Hello world'        # это не правильно !
# if ' ' in s2:             # нужно пользоваться функцыями
#     s2 = s2.upper()       
# else:
#     s2 = s2.lower()
# print(s2)
# def hello():   # defing oпределять 
#     print ('Hello')
# hello()

# def hello(name, word):   # defing oпределять 
#     print ('Hello, ' + name + '. Say' + word)
# hello('Jhon', 'hi')
# hello('Kety', 'Hello')

from typing import get_type_hints


def get_sum(a, b):
    return(a + b)   # хорошей практикой возвращать результат, а не печатать 

# x= 2
# y= 5
# get_sum(1, 3)
# get_sum(x, y)

# res = len('Hello') # возвращает результат, количество символов в тексте
# print (res)

print (get_sum(1, 2))


def hi():
    print ('HI')

hi()        # Правильный вызов функцции 
print(hi()) # неявно возвращает нон

# HW оформить прошлые задания в виде функции работай с параметрами 
