class Person:
    
    # name = 'John'

    def __init__(self, name) -> None:   #
        self.name = name                # способ передачи с помощью параметра, теперь имена пишутся в ()

    def print_info(self):
        print(f'Hello, my name is {self.name}')
