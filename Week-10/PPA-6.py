class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_info(self):
        print(f'({self.x},{self.y})')

    def scale(self, s):
        self.x *= s
        self.y *= s

    def reflect_about_X(self):
        self.y *= -1

    def reflect_about_Y(self):
        self.x *= -1

    def add(self, V):
        return Vector(self.x + V.x, self.y + V.y)
