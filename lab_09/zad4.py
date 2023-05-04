class Point:
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f'Point({self.x},{self.y})'

    def __mul__(self, other):
        return Point(self.x*other,self.y*other)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

if __name__=="__main__":
    p1 = Point(21, 37)
    p2 = Point(21.5, 37.5)
    p3 = Point(42, 74)

    print(p1 == p2)
    print(p1 == p3)