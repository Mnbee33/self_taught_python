class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created")

    def rot(self, days, temp):
        """Temp is Celsius"""
        self.mold = days * temp

orange1 = Orange(200, "light orange")
print(orange1.mold)

orange1.rot(10, 37)
print(orange1.mold)
