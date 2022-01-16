## Cap 7 - Classes
# EX3 - class CIRCLE

import math


class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def get_perimeter(self):
        return 2 * self.radius * math.pi

    def get_area(self):
        return self.radius * self.radius * math.pi

    def get_radius(self, radius):
        self.radius = radius
