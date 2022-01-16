## Cap 7 - Classes
# EX3 - class CIRCLE

from C7circle import Circle

def main():
    my_circle = Circle()

    # print areas for radius 1, 2, 3, 4 and 5
    n = 5
    print_areas(my_circle, n)

    # display my_circle radius and times
    print("\nRadius is", my_circle.radius)
    print("n is", n)


# print table of areas for radius
def print_areas(c, times):
    print("Radius \t\tArea")
    while times >= 1:
        print(c.radius, " \t\t", c.get_area())
        c.radius = c.radius + 1
        times = times - 1


main()

