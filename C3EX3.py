## Cap 3 - Mathematical functions, strings and objects
# C3EX2 Drawing shapes

import turtle

turtle.pensize(3) #set the thickness for 3 pixels
turtle.penup()
turtle.goto(-200, -50)
turtle.pendown()
turtle.circle(40, steps = 3) #draw a triangle

turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.circle(40, steps = 4) #draw a square

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.circle(40, steps = 5) #draw a pentagon

turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.circle(40, steps = 6) #draw a hexagon

turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.circle(40) #draw a circle

turtle.done()






