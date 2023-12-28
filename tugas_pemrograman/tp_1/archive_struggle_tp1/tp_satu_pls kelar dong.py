import turtle
from tkinter import messagebox

# Initial set for turtle object
mario = turtle.Turtle()
mario.speed(0)

# Set the color
brick_color = "#CA7F65"
head_brick_color = "#693424"

# Asking user the amount of tower to build
valid = False
while not valid:
    tower_amount = turtle.textinput("Build the tower!", "Enter the amount of tower(s) you want to build (at least 1)")

    # Validate the input
    if tower_amount is None:
        messagebox.showinfo("The value is none!", "Please provide a value.")
        continue

    if not tower_amount.isdigit():
        messagebox.showinfo("Invalid input!", "The amount of tower must be a positive integer. Please re-enter the input")
        continue

    tower_amount = int(tower_amount)

    if tower_amount < 1:
        messagebox.showinfo("Invalid input!", "The amount of towers must be at least 1. Please re-enter the input")
        continue

    valid = True

# The program reach here if user want to build >1 towers
if tower_amount > 1: 

    # Asking the user the distance between towers
    valid = False
    while not valid:
        tower_distance = turtle.textinput("Distance between towers!", "Enter the distance between towers (between 2 and 5)")

        # Validate the input
        if tower_distance is None:
            messagebox.showinfo("The value is none!", "Please provide a value.")
            continue

        if not tower_distance.isdigit():
            messagebox.showinfo("Invalid input!", "The distance between towers must be a positive integer. Please re-enter the input")
            continue

        tower_distance = int(tower_distance)

        if tower_distance < 2 or tower_distance > 5:
            messagebox.showinfo("Invalid input!", "The distance between towers must be between 2 and 5. Please re-enter the input.")
            continue

        valid = True

    # Asking the user the difference of layer between each tower
    valid = False
    while not valid:
        layer_differences = turtle.textinput("Layer differences!", "Enter the number of layer differences between each tower (between 2 and 5)")

        # Validate the answer
        if layer_differences is None:
            messagebox.showinfo("The value is none!", "Please provide a value.")
            continue

        if not layer_differences.isdigit():
            messagebox.showinfo("Invalid input!", "The number of layer differences must be a positive integer. Please re-enter the input")
            continue

        layer_differences = int(layer_differences)

        if layer_differences < 2 or layer_differences > 5:
            messagebox.showinfo("Invalid input!", "The number of layer differences must be between 2 and 5. Please re-enter the input.")
            continue

        valid = True

# Asking the user the length of each brick
valid = False
while not valid:
    one_brick_width = turtle.textinput("Width of the brick!", "Enter the width of the brick (integer)")

    # Validate the input
    if one_brick_width is None:
        messagebox.showinfo("The value is none!", "Please provide a value.")
        continue

    if not one_brick_width.isdigit():
        messagebox.showinfo("Invalid input!", "The width of brick must be a positive integer. Please re-enter the input")
        continue

    one_brick_width = int(one_brick_width)

    if one_brick_width > 35:
        messagebox.showinfo("Ups, it exceeds!", "The maximum value for the width is 35. Please re-enter the input!")
    
    else:
        valid = True

# Asking the user the height of each brick
valid = False
while not valid:
    one_brick_height = turtle.textinput("Height of the brick!", "Enter the height of the brick (integer)")

    # Validate the answer
    if one_brick_height is None:
        messagebox.showinfo("The value is none!", "Please provide a value.")
        continue

    if not one_brick_height.isdigit():
        messagebox.showinfo("Invalid input!", "The height of brick must be a positive integer. Please re-enter the input")
        continue

    one_brick_height = int(one_brick_height)

    if one_brick_height > 25:
        messagebox.showinfo("Ups, it exceeds!", "The maximum value for the height is 25. Please re-enter the input!")
    
    else:
        valid = True

# Asking the user the amount of layer for the initial tower
valid = False
while not valid:
    first_tower_layer = turtle.textinput("First tower's layer!", "Enter the amount of layer for the first tower (integer)")

    if first_tower_layer is None:
        messagebox.showinfo("The value is none!", "Please provide a value.")
        continue

    if not first_tower_layer.isdigit():
        messagebox.showinfo("Invalid input!", "The amount of layer must be a positive integer. Please re-enter the input")
        continue

    first_tower_layer = int(first_tower_layer)

    if first_tower_layer > 25:
        messagebox.showinfo("Ups, it exceeds!", "The maximum value for the amount of layer is 25. Please re-enter the input!")
    
    else:
        valid = True

# Asking the user the width of each tower's body (in bricks)
valid = False
while not valid:
    layer_width = turtle.textinput("Width of the layer!", "Enter the width of the layer (integer)")

    if layer_width is None:
        messagebox.showinfo("The value is none!", "Please provide a value.")
        continue

    if not layer_width.isdigit():
        messagebox.showinfo("Invalid input!", "The width of layer must be a positive integer. Please re-enter the input")
        continue

    layer_width = int(layer_width)

    if layer_width > 10:
        messagebox.showinfo("Ups, it exceeds!", "The maximum value for the width is 10 bricks. Please re-enter the input!")
    
    else:
        valid = True

# Calculate the starting position (x, y) with the given formula
begin_x = -(tower_amount - 1) * (one_brick_height + tower_distance) * (one_brick_width / 2)
begin_y = -(tower_amount - 1) * (layer_differences * one_brick_width / 2)

bricks = 0

for i in range(tower_amount):
    mario.penup()
    mario.goto(begin_x, begin_y)
    mario.pendown
    for j in range(first_tower_layer):
       turtle.

        for k in range(2):
            mario.fillcolor(brick_color)
            mario.begin_fill()
            mario.forward(one_brick_width)
            mario.left(90)
            mario.forward(one_brick_width)
            mario.left(90)
            mario.end_fill()
        begin_x += one_brick_width
    
    # The tower's head
    mario.penup()
    mario.goto(begin_x, begin_y)
    mario.pendown()
    mario.fillcolor(head_brick_color)
    mario.begin_fill()

    for l in range(2):
        mario.forward(one_brick_width)
        mario.left(90)
        mario.forward(one_brick_height)
        mario.left(90)
    
    mario.end_fill()

    first_tower_layer += layer_differences
    begin_x += one_brick_width * 2

mario.hideturtle()
turtle.done()

       

