# Модули в Python
# принято разбивать на логические части которые будут взаимодействовать друг с другом 
# их возможно импортировать или установить менеджер pip аналог composer 
# https://docs.python.org/3/library
# module OS 

# переписать игру угадай число, с модулем rendom. 

import os #, random # лучше каждый модуль отдельно записывать
# import random as r # возможно использовать псевдонимы
from random import randint, shuffle


print(os.getcwd())
# print(r.randint(1, 100)) # генерируем случайное число 

print(randint(1, 100))
l = [1, 2, 3, 4, 5]
shuffle(l)      # перемешать все значения 
print(l)