# Инкапсуляция это сокрытие чего либо. одно из поведений в ООП
# позволяет предотваратить прямой доступ к атрибутам обекта 

from classes import Person

person1 = Person('John')
person1.print_info()

person2 = Person('Katty')
person2.age = 30
person2.print_info()