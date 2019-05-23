class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        return "I am a shape"

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def caluculate_perimeter(self):
        return self.width * 2 + self.length * 2

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def caluculate_perimeter(self):
        return self.length * 4

    def change_size(self, size):
        self.length += size

print("--No.1--")
a_rectangle = Rectangle(2, 3)
print(a_rectangle.caluculate_perimeter())

a_square = Square(3)
print(a_square.caluculate_perimeter())

print("--No.2--")
a_square.change_size(-1)
print(a_square.caluculate_perimeter())

print("--No.3--")
print(a_rectangle.what_am_i())
print(a_square.what_am_i())


class Rider:
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse

class Horse:
    def __init__(self, name):
        self.name = name

print("--No.4--")
deep_impact = Horse("Deep Impact")
yutaka = Rider("Yutaka", deep_impact)
print(yutaka.horse.name)
