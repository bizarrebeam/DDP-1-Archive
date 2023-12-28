import turtle
from tkinter import *
from tkinter import messagebox

# Initial set

# Asking user how many towers they want to build
amount_of_tower = turtle.textinput("Build the tower!", "Enter the amount of towers you want to build (integer)")

valid = False
while not valid:
    if amount_of_tower is not None and amount_of_tower.isdigit():
        amount_of_tower = int(amount_of_tower)

        # If user chooses to build more than one tower
        if amount_of_tower > 1:
            tower_distance = turtle.textinput("Enter the distance between each tower (integer)")
            
            if tower_distance is not None and tower_distance.isdigit():
                tower_distance = int(tower_distance)

                if tower_distance < 2 or tower_distance > 5:
                    messagebox.showinfo("Invalid input!", "Tower distance must be between 2 and 5. Please provide a valid input.")
            else:
                messagebox.showinfo("Invalid input!", "Tower distance must be a positive integer. Please provide a valid input.")

            # Asking user the differences between each tower's layer
            delta_of_layer = turtle.textinput("Enter the number of layer differences between each tower (integer)")

            if delta_of_layer is not None and delta_of_layer.isdigit():
                delta_of_layer = int(delta_of_layer)

                if delta_of_layer < 2 or delta_of_layer > 5:
                    messagebox.showinfo("Invalid input!", "Layer difference must be between 2 and 5. Please provide a valid input.")
            else:
                messagebox.showinfo("Invalid input!", "Layer difference must be a positive integer. Please provide a valid input.")
    else:
        messagebox.showinfo("Invalid input!", "The amount of tower must be a positive integer. Please provide a valid input.")

# Asking user the length of each brick    
height_of_brick = turtle.textinput("Modify your brick!", "Enter the height of the brick (integer)")

if height_of_brick is not None and height_of_brick.isdigit():
    height_of_brick = int(height_of_brick)

    if height_of_brick > 25:
        messagebox.showinfo("Invalid input!", "The maximum height is 25. Please provide a valid input.")
    elif height_of_brick < 1:
        messagebox.showinfo("Invalid input!", "Height must be 1 or greater. Please provide a valid input.")
else:
    messagebox.showinfo("Invalid input!", "The height of brick must be a positive integer. Please provide a valid input.")

# Asking user the width of each brick
width_of_brick = turtle.textinput("Modify your brick!", "Enter the width of the brick (integer)")

if width_of_brick is not None and width_of_brick.isdigit():
    width_of_brick = int(width_of_brick)

    if width_of_brick > 25:
        messagebox.showinfo("Invalid input!", "The maximum width is 25. Please provide a valid input.")
    elif width_of_brick < 1:
        messagebox.showinfo("Invalid input!", "Width must be 1 or greater. Please provide a valid input.")
else:
    messagebox.showinfo("Invalid input!", "The width of brick must be a positive integer. Please provide a valid input.")
        
# Asking user the amount of layer for the first (initial) tower
first_tower_layer = turtle.textinput("The first tower!", "Enter the amount of layer for the first tower (integer)")

if first_tower_layer is not None and first_tower_layer.isdigit():
    first_tower_layer = int(first_tower_layer)

    if first_tower_layer > 25:
        messagebox.showinfo("Invalid input!", "The maximum number of layers is 25. Please provide a valid input.")
    elif first_tower_layer < 1:
        messagebox.showinfo("Invalid input!", "Number of layers must be 1 or greater. Please provide a valid input.")
else:
    messagebox.showinfo("Invalid input!", "The layer for tower must be a positive integer. Please provide a valid input.")
        
# Asking user the length of brick layer
width_of_layer = turtle.textinput("Length of the layer!", "Enter the length of the layer (integer)")

if width_of_layer is not None and width_of_layer.isdigit():
    width_of_layer = int(width_of_layer)

    if width_of_layer > 10:
        messagebox.showinfo("Invalid input!", "The maximum width is 10 bricks. Please provide a valid input.")
    elif width_of_layer < 1:
        messagebox.showinfo("Invalid input!", "Width must be 1 or greater. Please provide a valid input.")
else:
    messagebox.showinfo("Invalid input!", "The width of the layer must be a positive integer. Please provide a valid input.")
