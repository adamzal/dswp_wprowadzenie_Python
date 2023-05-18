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


points = [Point(1, 2), Point(3, 4), Point(5, 6)]

with open("points.pickle", "wb") as file:
    pickle.dump(points, file)

with open("points.pickle", "rb") as file:
    loaded_points = pickle.load(file)

for point in loaded_points:
    print(point)
