class Point:
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)


if __name__=="__main__":
    p = Point(21,37)
    print(p.x, p.y)

    p = Point(0.21,0.37)
    print(p.x, p.y)