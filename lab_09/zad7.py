from zad4 import Point

class Polygon:
    def __init__(self, points=[]):
        self.points = points

    def add_point(self, point):
        if isinstance(point, Point):
            self.points.append(point)

    def __str__(self):
        return 'Polygon: '+''.join([f'Point({p.x},{p.y}) ' for p in self.points])

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.points[item]
        elif isinstance(item, slice):
            return Polygon(self.points[item])
        else:
            raise ValueError("Expected an integer or slice object")


if __name__=="__main__":
    p1 = Point(0, 0)
    p2 = Point(0, 1)
    p3 = Point(1, 0)
    p4 = Point(1, 1)

    poly = Polygon()
    poly.add_point(p1)
    poly.add_point(p2)
    poly.add_point(p3)
    poly.add_point(p4)

    print(poly[1:3])

