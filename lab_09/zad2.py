class Point:
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f'Point({self.x},{self.y})'


if __name__=="__main__":
    p = Point(21, 37)
    print(p)
