class Person:
    
    # name = 'John'

    def __init__(self, name) -> None:   # метод для инициализации атрибутов класса для передачи параметров
        self.name = name                # способ передачи с помощью параметра, теперь имена пишутся в ()
        self.age = 20

    def print_info(self):               # self указывает на объект и берет свойства у конкретного объекта 
        print(f'Name: {self.name}, Age: {self.age}')
