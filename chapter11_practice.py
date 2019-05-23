import math

class Apple:
    def __init__(self):
        self.weight = 100
        self.color = "red"
        self.sweetness = 15
        self.brand = "Ourin"

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi

print("--No.2--")
circle = Circle(4)
print(circle.area())

class Triangle:
    def __init__(self, bottom, height):
        self.bottom = bottom
        self.height = height

    def area(self):
        return self.bottom * self.height / 2

print("--No.3--")
tri = Triangle(3, 4)
print(tri.area())

class Hexagon:
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6

print("--No.4--")
hexagon = Hexagon(1, 2, 3, 4, 5, 6)
print(hexagon.calculate_perimeter())
