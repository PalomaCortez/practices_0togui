## Cap 3 - Mathematical functions, strings and objects
# C3EX2 Drawing shapes

import turtle

turtle.pensize(3) #set the thickness for 3 pixels
turtle.penup()
turtle.goto(-200, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.circle(40, steps = 3) #draw a triangle
turtle.end_fill() #fill the shape

turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color("blue")
turtle.circle(40, steps = 4) #draw a square
turtle.end_fill()

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color("green")
turtle.circle(40, steps = 5) #draw a pentagon
turtle.end_fill()

turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color("yellow")
turtle.circle(40, steps = 6) #draw a hexagon
turtle.end_fill()

turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color("purple")
turtle.circle(40) #draw a circle
turtle.end_fill()
turtle.color("green")
turtle.penup()
turtle.goto(-100, 50)
turtle.pendown()
turtle.write("Cool colorful shapes",
             font = ("Times", 18, "bold"))
turtle.hideturtle()

turtle.done()






