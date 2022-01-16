## Cap 6 - functions
# EX6 - Usefull turtle Function

import turtle

# Draw a ligne from (x1, y1) to (x2,y2)
def draw_line(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)


# Write a string on a specified location ( x, y)
def write_text(s, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(s)


# Draw a point at a specified location ( x, y)
def draw_point(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()


# Draw a circle centered at (x,y) with the specified radius
def draw_circle(x = 0, y = 0, radius = 10):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.circle(radius)


# Draw a rectangle at (x, y) with the specified width ans height
def draw_rectangle(x = 0, y = 0, width = 10, height = 10):
    turtle.penup()
    turtle.goto(x + width/2, y + height/2)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
