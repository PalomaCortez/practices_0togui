## C10 Inheritance and Polymorphism
# EX5 Polymorphism

from C10EX2 import Circle
from C10EX3 import Rectangle


def main():
    # display circle and rectangle properties
    c = Circle(4)
    r = Rectangle(1, 3)
    display_object(c)
    display_object(r)
    print("Are the circle and rectangle the same size?", is_same_area(c, r))


# display geometric properties
def display_object(g):
    print(g.__str__())


# compare areas of two geometric objects
def is_same_area(g1, g2):
    return g1.get_area() == g2.get_area()


main()
