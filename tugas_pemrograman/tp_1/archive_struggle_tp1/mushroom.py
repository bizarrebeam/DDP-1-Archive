import turtle

# Set up the turtle
mario = turtle.Turtle()
mario.speed(1)

# Mushroom cap (red)
mario.penup()
mario.goto(25, 0)
mario.pendown()
mario.begin_fill()
mario.color("red")
mario.setheading(90)  # Set the heading to 90 degrees (upwards)
mario.circle(50, 180)  # Use a positive angle to draw horizontally
mario.end_fill()

# Mushroom stem (light brown)
mario.penup()
mario.goto(5, 0)
mario.pendown()
mario.begin_fill()
mario.color("#D2B48C")
mario.forward(60)
mario.right(90)
mario.forward(60)
mario.right(90)
mario.forward(60)
mario.right(90)
mario.forward(60)
mario.end_fill()

# Close the turtle graphics window on click
turtle.exitonclick()
