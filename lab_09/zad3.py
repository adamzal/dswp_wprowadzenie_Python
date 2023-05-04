class Point:
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f'Point({self.x},{self.y})'

    def __mul__(self, other):
        return Point(self.x*other,self.y*other)

p=Point(21, 37)
print(p)
print(p*2)