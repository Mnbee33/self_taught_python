class Square:
    pass
print(Square)


class Rectangle:
    rectangles = []
    
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.rectangles.append((self.width, self.length))

    def print_size(self):
        print("{} by {}".format(self.width, self.length))

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.rectangles)


class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

lion = Lion("Dilbert")
print(lion)


class AlwaysPositive:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return abs(self.number + other.number)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)
print(x + y)


class Person:
    def __init__(self):
        self.name = "Bob"

bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)

x = 10
if x  is None:
    print("x is None :(")
else:
    print("x is not None")

x = None
if x  is None:
    print("x is None :(")
else:
    print("x is not None")

