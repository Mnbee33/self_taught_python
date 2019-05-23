class Square:
    square_list = []
    def __init__(self, length):
        self.length = length
        self.square_list.append(self)

    def __repr__(self):
        return "{len} by {len} by {len} by {len}".format(len = self.length)
    
s1 = Square(29)
s2 = Square(30)
print(s1.square_list)
print(s1)

def is_equal(object1, object2):
    return object1 is object2

print(is_equal(s1, s1))
print(is_equal(s1, s2))
