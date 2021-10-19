# наследование  позволяет содавать новый класс на основе существующего и наследовать от родительского класса все публичные методы и свойства
# 
from classes import Person

person1 = Person('John')
print(person1.age)
person1.age = 35
person1.print_info()
