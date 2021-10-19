# наследование  позволяет содавать новый класс на основе существующего 
from classes import Person

person1 = Person('John')
print(person1.age)
person1.age = 35
person1.print_info()
