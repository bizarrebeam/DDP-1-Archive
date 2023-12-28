import turtle
from tkinter import messagebox

# Initial set for the screen display
screen = turtle.Screen()
screen.setup(width = 1000, height = 700)

# Initial set for the turtle object: Mario builds its own tower(s)!
mario = turtle.Turtle()
mario.speed(0) # Set to the fastest speed

# Initial set for variables needed
tower_distance = 0
layer_differences = 0
bricks = 0
tower = 0

# Asking user the amount of tower to build
valid = False
while not valid:
    tower_amount = turtle.textinput("Build the tower!", "Enter the amount of tower(s) you want to build! (at least 1 tower)")

    # Validate the input
    if tower_amount is None: 
        messagebox.showinfo("The value is none :(", "Please provide a value.")
        continue

    if not tower_amount.isdigit(): 
        messagebox.showinfo("Invalid input :(", "The amount of tower must be a positive integer. Please re-enter the input")
        continue
    
    tower_amount = int(tower_amount)

    if tower_amount < 1: 
        messagebox.showinfo("Invalid input :(", "The amount of towers must be at least 1. Please re-enter the input")
        continue

    valid = True

# The program reach here if user want to build >1 towers
if tower_amount > 1: 

    # Asking the user the distance between towers
    valid = False
    while not valid:
        tower_distance = turtle.textinput("Distance between towers!", "Enter the distance between towers (min 2 and max 5 pixel)")

        # Validate the input
        if tower_distance is None: 
            messagebox.showinfo("The value is none :(", "Please provide a value.")
            continue

        if not tower_distance.isdigit(): 
            messagebox.showinfo("Invalid input :(", "The distance between towers must be a positive integer. Please re-enter the input")
            continue

        tower_distance = int(tower_distance)

        if tower_distance < 2 or tower_distance > 5:
            messagebox.showinfo("Invalid input :(", "The distance between towers must be between 2 and 5. Please re-enter the input")
            continue

        valid = True

    # Asking the user the difference of layer between each tower
    valid = False
    while not valid:
        layer_differences = turtle.textinput("Layer differences!", "Enter the number of layer differences between each tower (min 2 and max 5 pixel)")

        # Validate the answer
        if layer_differences is None: 
            messagebox.showinfo("The value is none :(", "Please provide a value.")
            continue

        if not layer_differences.isdigit(): 
            messagebox.showinfo("Invalid input :(", "The number of layer differences must be a positive integer. Please re-enter the input")
            continue

        layer_differences = int(layer_differences)

        if layer_differences < 2 or layer_differences > 5:
            messagebox.showinfo("Invalid input :(", "The number of layer differences must be between 2 and 5. Please re-enter the input.")
            continue

        valid = True

# Asking the user the length of each brick
valid = False
while not valid:
    one_brick_width = turtle.textinput("Width of the brick!", "Enter the width of the brick (max 35 pixel)")

    # Validate the input
    if one_brick_width is None: 
        messagebox.showinfo("The value is none :(", "Please provide a value.")
        continue

    if not one_brick_width.isdigit(): 
        messagebox.showinfo("Invalid input :(", "The width of brick must be a positive integer. Please re-enter the input")
        continue

    one_brick_width = int(one_brick_width)

    if one_brick_width > 35:
        messagebox.showinfo("Ups, it exceeds :(", "The maximum value for the width is 35. Please re-enter the input!")
    
    else:
        valid = True

# Asking the user the height of each brick
valid = False
while not valid:
    one_brick_height = turtle.textinput("Height of the brick!", "Enter the height of the brick (max 25 pixel)")

    # Validate the answer
    if one_brick_height is None: 
        messagebox.showinfo("The value is none :(", "Please provide a value.")
        continue

    if not one_brick_height.isdigit(): 
        messagebox.showinfo("Invalid input :(", "The height of brick must be a positive integer. Please re-enter the input")
        continue

    one_brick_height = int(one_brick_height)

    if one_brick_height > 25:
        messagebox.showinfo("Ups, it exceeds :(", "The maximum value for the height is 25. Please re-enter the input!")
    
    else:
        valid = True

# Asking the user the amount of layer for the first tower
valid = False
while not valid:
    first_tower_layer = turtle.textinput("First tower's layer!", "Enter the amount of layer for the first tower")

    if first_tower_layer is None: 
        messagebox.showinfo("The value is none :(", "Please provide a value.")
        continue

    if not first_tower_layer.isdigit(): 
        messagebox.showinfo("Invalid input :(", "The amount of layer must be a positive integer. Please re-enter the input")
        continue

    first_tower_layer = int(first_tower_layer)

    if first_tower_layer > 25:
        messagebox.showinfo("Ups, it exceeds :(", "The maximum value for the amount of layer is 25. Please re-enter the input!")
    
    else:
        valid = True

# Asking the user the width of each tower's body (in bricks)
valid = False
while not valid:
    layer_width = turtle.textinput("Width of the layer!", "Enter the width of the layer (in bricks)")

    if layer_width is None:
        messagebox.showinfo("The value is none :(", "Please provide a value.")
        continue

    if not layer_width.isdigit():
        messagebox.showinfo("Invalid input :(", "The width of layer must be a positive integer. Please re-enter the input")
        continue

    layer_width = int(layer_width)

    if layer_width > 10:
        messagebox.showinfo("Ups, it exceeds :(", "The maximum value for the width is 10 bricks. Please re-enter the input!")
    
    else:
        valid = True

# Calculate the total width of all towers and the spacing between them for screen adjustment
total_tower_width = (tower_amount) * (layer_width + tower_distance) * (one_brick_width)

# Calculate the total height of all towers for screen adjustment
total_tower_height = tower_amount * layer_differences * one_brick_height

# Calculate the starting position (x, y) 
begin_x = -total_tower_width // 2  
begin_y = -total_tower_height // 2  

# Loop to build each tower
for tower in range(tower_amount):

    # Starts from the begin coordinates
    at_x = begin_x
    at_y = begin_y

    # Loop to build each layer of bricks that builds the tower vertically
    for layer in range(first_tower_layer):

        # Loop to build bricks for the tower's width
        for i in range(layer_width):

            # Build the brick starts from the low corner of the tower
            mario.penup()
            mario.goto(at_x, at_y)
            mario.pendown()
            mario.pencolor("black")
            mario.fillcolor("#CA7F65")
            mario.begin_fill()
            for side in range(2):
                mario.forward(one_brick_width)
                mario.right(90)
                mario.forward(one_brick_height)
                mario.right(90)
            mario.end_fill()
            bricks += 1 # Count the drawn bricks

            # Determine the next x coordinate for the adjacent bricks
            at_x += one_brick_width

        # Move up to the next layer
        at_x -= (layer_width * one_brick_width) # Move back to the left-most position
        at_y += one_brick_height  # Move up one layer
    
    # Calculate the starting position for the tower's head
    head_x = at_x - (one_brick_width // 2) # The tower head has one excess brick
    head_y = at_y 

    # Draw the tower's head
    for i in range(layer_width + 1): 
        mario.penup()
        mario.goto(head_x, head_y)
        mario.pendown()
        mario.pencolor("black")
        mario.fillcolor("#693424")
        mario.begin_fill()
        for side in range(2):
            mario.forward(one_brick_width)
            mario.right(90)
            mario.forward(one_brick_height)
            mario.right(90)
        mario.end_fill() 
        if i < layer_width:
            head_x += one_brick_width
        bricks += 1

    # Calculate the position for the mushroom's stem
    stem_x = at_x + (layer_width * (one_brick_width) // 2) - (3 *one_brick_width // 4)
    stem_y = head_y + (3 * one_brick_height // 2)

    # Draw the mushroom's stem upper the each tower's head
    mario.penup()
    mario.goto(stem_x, stem_y)
    mario.pencolor("black")
    mario.pendown()
    mario.fillcolor("#D2B48C")
    mario.begin_fill()
    for side in range(2):
        mario.forward(3 * one_brick_width // 2)
        mario.right(90)
        mario.forward(3 * one_brick_height // 2)
        mario.right(90)
    mario.end_fill()
    # Move to the next mushroom in the next tower
    stem_x += ((7 - (5 * one_brick_width) // 4) + tower_distance) 

    # Calculate the position for the mushroom's cap
    cap_x = head_x + (layer_width * one_brick_width // 2) - (3 * one_brick_width)
    cap_y = head_y + (3 * one_brick_height // 2)

    # Draw the mushroom's cap upper the each mushroom's stems
    mario.penup()
    mario.goto(cap_x, cap_y)
    mario.pencolor("black")
    mario.pendown()
    mario.fillcolor("red")
    mario.begin_fill()
    mario.setheading(90)  # Set the heading upwards to draw a half of circle
    mario.circle((3 *one_brick_width // 2), 180)
    mario.setheading(0)  # Set back angle to draw horizontally
    mario.forward(3 *one_brick_width)
    mario.end_fill()
    # Move to the next mushroom in the next tower
    cap_x += ((3 * one_brick_width) + (layer_width * one_brick_width // 2) + tower_distance)

    # Calculate starting position for the next tower
    begin_x += (layer_width + tower_distance + 1) * one_brick_width  # Adjust for the tower's head and distance between towers
    begin_y =  -total_tower_height // 2
    
    # Increment the layer for the next tower
    first_tower_layer += layer_differences

# Adjust the starting position for the next layer in the tower's body
at_y -= one_brick_height

# Hide the mario cursor after build all the tower(s)
mario.hideturtle()

# Move the cursor under the tower
mario.penup()
mario.goto(0, -total_tower_height // 2 - 60) 
mario.pendown()

# Display the message with the number of towers and bricks built
message = f"{tower_amount} Super Mario Towers have been built with a total of {bricks} bricks"
mario.write(message, align = "center", font = ("Verdena", 10, "bold"))

# Keep the window open until clicked
turtle.exitonclick()

   
        




        



        

