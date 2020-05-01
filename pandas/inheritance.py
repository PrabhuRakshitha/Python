class A(object):
    def __init__(self):
        self.x = 1
    def say(self):
        print('hello A is here')

class B (A):
    def __init__(self):
        super().__init__()
        self.y = 2

    def talk(self):
        print('B is here')


if __name__ == "__main__":
    obj = B()
    print(obj.y)
    print(obj.x)
    obj.say()
    obj.talk()

