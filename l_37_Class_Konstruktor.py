# конструктор класса - что такое конструктор? 

from classes import Person  # два варианта импорта класса из файла classses.py 
# import classes              # эта запись короче и импортирует все классы 

person1 = Person('John')
person1.print_info()

person2 = Person('Katty')
# person2.name = 'Katty'
person2.print_info()