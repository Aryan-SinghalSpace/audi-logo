import turtle

# Set up the turtle
turtle.speed(2)
turtle.pensize(5)
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()

# Draw the circles
for i in range(4):
    turtle.circle(50)
    turtle.penup()
    turtle.forward(80)
    turtle.pendown()

# Hide the turtle and show the drawing
turtle.hideturtle()
turtle.done()
