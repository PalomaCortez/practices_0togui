## Cap 5 - Loops
#EX5 - Random Walk

import turtle
from random import randint

turtle.speed(1) #cset turtle speed to the slowest

# Draw 16x16 lattice
turtle.color("gray")
x = -80
for y in range(-80, 80 + 1, 10):
    turtle.penup()
    turtle.goto(x,y) # draw a horizontal line
    turtle.pendown()
    turtle.forward(160)

y = 80
turtle.right(90)
for x in range(-80, 80 + 1, 10):
    turtle.penup()
    turtle.goto(x,y) # draw a vertical line
    turtle.pendown()
    turtle.forward(160)

turtle.pensize(3)
turtle.color("red")


turtle.penup()
turtle.goto(0, 0) # to go to the center
turtle.pendown()

x = y = 0 #current location at the center of the lattice
while abs(x) < 80 and abs(y) < 80:
    r = randint(0,3)
    if r == 0:
        x += 10 #walk right
        turtle.setheading(0)
        turtle.forward(10)
    elif r == 1:
        y -= 10 #walk down
        turtle.setheading(270)
        turtle.forward(10)
    elif r == 2:
        x -= 10 #walk left
        turtle.setheading(180)
        turtle.forward(10)
    elif r == 3:
        y += 10 #walk up
        turtle.setheading(90)
        turtle.forward(10)

turtle.done()
