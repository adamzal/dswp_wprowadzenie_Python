import pickle


class Point:
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f'Point({self.x},{self.y})'

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

point = Point(3, 5)

with open("point.pickle", "wb") as file:
    pickle.dump(point, file)

with open("point.pickle", "rb") as file:
    loaded_point = pickle.load(file)

print(loaded_point)
