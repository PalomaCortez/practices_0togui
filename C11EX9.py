## C11 Files and Exception Handling
# Ex8 Test Circle exception

from C11EX8 import Circle

try:
    c1 = Circle(5)
    print("c1`s area is", c1.get_area())

    c3 = Circle(0)
    print("c3`s area is", c3.get_area())

    c2 = Circle(-5)
    print("c2 area is", c2.get_area())

except RuntimeError:
    print("Invalid radius")
