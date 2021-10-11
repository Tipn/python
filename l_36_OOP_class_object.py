# обектно ориентированное программирование 
# основные концепции Обекты и классы 
# Класс - это тип описывающий устройство объектов (Чертеж) (схема) (набросок) по которой создаются объекты 
# Объект - это екземпляр класса (''.)
# у объекта есть свойства (переменные) 

class A:
    property1 = 'Propery 1'
    property2 = 'Propery 2'
    name = 'geest'

    def say_hi(self, name=''):   # self является обязательнымчтоб редактор понимал на какой обект ссылться 
        if name:
            return 'Hi, ' + name
        else:
            return 'Hello, ' + self.name



a = A() # был создан объект<__main__.A object at 0x7f22c67d6040>
b = A()
# a.property1 = 'Propery 1'
# a.property2 = 'Propery 2'
# print(a)
print(a.property1)  # создал свойство
print(a.say_hi()) # name обязательный параметр
print(b.say_hi('Pasha'))
