import turtle
from tkinter import messagebox

valid = False
while not valid:
    tower_amount = turtle.textinput("Tower to build!", "Enter the amount of towers you want to build (at least 1)")

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

    if tower_amount > 1:
        tower_distance = turtle.textinput("Distance between towers!", "Enter the distance between towers (between 2 and 5)")

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

        layer_differences = turtle.textinput("Enter the number of layer differences between each tower (between 2 and 5)")

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

valid = False
while not valid:
    brick_length = turtle.textinput("Enter the length of the brick (integer)", "Enter the length of the brick (integer)")

    if brick_length is None:
        messagebox.showinfo("The value is none!", "Please provide a value.")
        continue

    if not brick_length.isdigit():
        messagebox.showinfo("Invalid input!", "The length of brick must be a positive integer. Please re-enter the input")
        continue

    brick_length = int(brick_length)

    if brick_length > 35:
        messagebox.showinfo("Ups, it exceeds!", "The maximum value for the length is 35. Please re-enter the input!")
    
    else:
        valid = True

valid = False
while not valid:
    brick_width = turtle.textinput("Enter the width of the brick (integer)", "Enter the width of the brick (integer)")

    if brick_width is None:
        messagebox.showinfo("The value is none!", "Please provide a value.")
        continue

    if not brick_width.isdigit():
        messagebox.showinfo("Invalid input!", "The width of brick must be a positive integer. Please re-enter the input")
        continue

    brick_width = int(brick_width)

    if brick_width > 25:
        messagebox.showinfo("Ups, it exceeds!", "The maximum value for the width is 25. Please re-enter the input!")
    
    else:
        valid = True

valid = False
while not valid:
    first_tower_layer = turtle.textinput("Enter the amount of layer for the first tower (integer)", "Enter the amount of layer for the first tower (integer)")

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

valid = False
while not valid:
    layer_length = turtle.textinput("Enter the length of the layer (integer)", "Enter the length of the layer (integer)")

    if layer_length is None:
        messagebox.showinfo("The value is none!", "Please provide a value.")
        continue

    if not layer_length.isdigit():
        messagebox.showinfo("Invalid input!", "The length of layer must be a positive integer. Please re-enter the input")
        continue

    layer_length = int(layer_length)

    if layer_length > 10:
        messagebox.showinfo("Ups, it exceeds!", "The maximum value for the length of layer is 10 bricks. Please re-enter the input!")
    
    else:
        valid = True
