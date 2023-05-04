class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __mul__(self, number):
        return Point(self.x * number, self.y * number)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and type(other) == Point

