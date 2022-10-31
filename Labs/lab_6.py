import dudraw
from random import random

# Setting canvas size
dudraw.set_canvas_size(800, 400)

# Setting scales
dudraw.set_x_scale(0, 800)
dudraw.set_y_scale(0, 400)

# Creating a for loop 
for i in range (4000):
    # Creating random numbers for the x and y values
    x_position = random()*800
    y_position = random()*400

    # Checking if the x value 'is' on the left third and setting the color to green
    if x_position < 266:
        dudraw.set_pen_color_rgb(80, 132, 89) # Green
    # Checking if the x and y values are in the top right third and setting the color to yellow
    elif x_position > 266 and y_position > 200:
        dudraw.set_pen_color_rgb(242, 212, 100) # Yellow
    # The only color left is red so the else statement sets the color to red
    else:
        dudraw.set_pen_color_rgb(197, 64, 60) # Red
    # Creating the circles
    dudraw.filled_circle(x_position, y_position, 10)
dudraw.show(10000)

