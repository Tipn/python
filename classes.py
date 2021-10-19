class Person:
    
    # name = 'John'

    def __init__(self, name, age) -> None:   # метод для инициализации атрибутов класса для передачи параметров
        self.name = name                # способ передачи с помощью параметра, теперь имена пишутся в ()
        # self.age = 20
        self.__age = age                 # приватная переменная 


    def print_info(self):               # self указывает на объект и берет свойства у конкретного объекта 
        print(f'Name: {self.name}, Age: {self.__age}')

# '''    # metod Getter setter
#     def get_age(self):
#         return self.__age

#     def set_age(self, value):       # метод сеттер
#         # self.__age = value          # способ разрешить передавать значения 
#         if value in range(1, 101):  # способ ограничить параметры ввода 
#             self.__age = value
#         else:
#             print('Wrong age')
# '''
    @property                   # метод геттер с дикоратором
    def age(self):
        return self.__age
    
    @age.setter                 # метод сеттер 
    def age(self, value):       #   будь внимателен!!
        if value in range(1, 101):  # способ ограничить параметры ввода 
            self.__age = value
        else:
            print('Wrong age')
# сначало идет Геттор после сеттор, иначе ошибка  

class Employee(Person):
    company = 'Google'

    def more_info(self):
        print(f'{self.name}, works in {self.company}')
