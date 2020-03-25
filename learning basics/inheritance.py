
class Animal:
    def speak(self):
        print('None')


class Cat(Animal):
    def speak(self):
        print('Meow ....!')


class Dog(Animal):
    def speak(self):
        print('wooof ....!')


class Seal(Cat, Dog):
    def __init__(self):
        self.name = 'sea dogo'


if __name__ == '__main__':
    obj1 = Seal()
    obj1.speak()

