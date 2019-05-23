class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"

    def public_method(self):
        pass

    def _unsafe_method(self):
        pass

class Shape:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def print_size(self):
        print("{} by {}".format(self.width, self.length))

my_shape = Shape(20, 25)
my_shape.print_size()


class Square(Shape):
    def area(self):
        return self.width * self.length

    def print_size(self):
        print("I am {} by {}".format(self.width, self.length))

a_square = Square(20, 20)
a_square.print_size()
print(a_square.area())

class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self, name):
        self.name = name

mick = Person("Mick")
stan = Dog("Stanley", "Bulldog", mick)
print(stan.owner.name)
