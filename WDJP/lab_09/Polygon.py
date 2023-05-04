from Point import Point

class Polygon:

    def __init__(self, points=None):
        if points is None:
            points = []
        self.points = points

    def add_point(self, point: Point):
        self.points.append(point)

    def __str__(self):
        return "Polygon[" + ', '.join([str(x) for x in self.points]) + "]"

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.points[key]
        elif isinstance(key, slice):
            return "[" + ', '.join([str(self.points[x]) for x in range(*key.indices(len(self.points)))]) + "]"
        else:
            raise TypeError("Argument not slice nor int")

