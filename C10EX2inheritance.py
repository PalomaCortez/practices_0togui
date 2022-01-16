## C10 Inheritance and Polymorphism
# EX2 adding inherit class

from C10EX1 import GeometricObject
import math


class Circle(GeometricObject):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_area(self):
        return self.__radius * self.__radius * math.pi

    def get_diameter(self):
        return 2 * self.__radius

    def get_perimeter(self):
        return self.get_diameter() * math.pi

    def print_circle(self):
        print(self.__str__() + ", radius: " + str(self.__radius))
