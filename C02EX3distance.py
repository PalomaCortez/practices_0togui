## Cap 2 - Elementary Programing
##C2Ex3 Computer distance Graphics

import turtle

# prompt the user for inputing two points
x1, y1 = eval(input("Enter x1 and y1 for point 1: "))
x2, y2 = eval(input("Enter x2 and y2 for point 2: "))

# compute the distance
distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# display two points and the connecting line
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.write("Point 1")
turtle.goto(x2,y2)
turtle.write("Point 2")

# move to the center of the line
turtle.penup()
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2)
turtle.write(distance)

turtle.done()

