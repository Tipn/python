# Модули в Python
# принято разбивать на логические части которые будут взаимодействовать друг с другом 
# их возможно импортировать или установить менеджер pip аналог composer 
# https://docs.python.org/3/library
# module OS 

# переписать игру угадай число, с модулем rendom. 

import os, random

print(os.getcwd())
print(random.randint(1, 100)) # генерируем случайное число 

