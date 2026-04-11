class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def distance_from_origin(self):
        return (self.x**2 + self.y**2)**0.5

    def __ge__(self, other):
        return self.distance_from_origin() >= other.distance_from_origin()


# objects
p1 = Point(3, 4)
p2 = Point(1, 1)

print("Distance:", p1 - p2)
print("p1 >= p2 ?", p1 >= p2)