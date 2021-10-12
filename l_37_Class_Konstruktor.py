# конструктор класса - что такое конструктор?
# классы принято выносить в оддельные подключаемые модули.   

from classes import Person  # вариант импорта класса Person из файла classses.py 
# import classes              # эта запись короче и импортирует все классы, но при вызове каждого класа нужно указывать его название 

person1 = Person('John')
person1.print_info()

person2 = Person('Katty')
# person2.name = 'Katty'
person2.print_info()