# наследование  позволяет содавать новый класс на основе существующего и наследовать от родительского класса все публичные методы и свойства
# 
from classes import Person, Employee

person = Person('Pavel', 30)
print(person.age)
person.age = 33
person.print_info()

employee = Employee('Nick', 30)
employee.print_info()
employee.more_info()        # Nick, works in Google
