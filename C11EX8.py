## C11 Files and Exception Handling
# Ex8 Circle exception

from C10EX1 import GeometricObject
import math


class Circle(GeometricObject):
    def __init__(self, radius):
        super().__init__()
        self.set_radius(radius)

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        if radius < 0:
            raise RuntimeError("Negative radius")
        else:
            self.__radius = radius

    def get_area(self):
        return self.__radius * self.__radius * math.pi

    def get_diameter(self):
        return 2 * self.__radius

    def get_perimeter(self):
        return 2 * self.__radius * math.pi

    def print_circle(self):
        print(self.__str__() + " radius: " + str(self.__radius))
