class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.classname = self.__class__.__name__

    def speak(self):
        print('Speaking...')


class Client(Person):
    def buy(self):
        print(f'{self.classname} buying... ')


class Student(Person):
    def studying(self):
        print(f'{self.classname} studying... ')
