# обектно ориентированное программирование 
# основные концепции Обекты и классы 
# Класс - это тип описывающий устройство объектов (Чертеж) (схема) (набросок) по которой создаются объекты 
# Объект - это екземпляр класса (''.)
# у объекта есть свойства (переменные) 

class A:
    property1 = 'Propery 1'
    property2 = 'Propery 2'


    def say_hi(self, name='guest'):   # self является обязательнымчтоб редактор понимал на какой обект ссылться 
        return 'Hi, ' + name


a = A() # был создан объект<__main__.A object at 0x7f22c67d6040>
b = A()
# a.property1 = 'Propery 1'
# a.property2 = 'Propery 2'
# print(a)
print(a.property1)  # создал свойство
print(a.say_hi('Pasha')) # name обязательный параметр
print(b.say_hi('John'))
