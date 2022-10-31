""" 
    File Name: platt_project4_animations.py
    Author: Ben Platt
    Date: 10/06/22
    Course: COMP 1351
    Assignment: Project 4
    Collaborators: None
    Internet Source: None
"""

# MUST PRESS G TO CHANGE COLORS


# Importing dudraw and random
import dudraw
import random


# Defining my function with 4 parameters x, y, w, and h
def my_animation(x:float, y:float, w:float, h:float):
    # Set canvas size to 500 by 500
    dudraw.set_canvas_size(500, 500)
    # Set the scales
    dudraw.set_x_scale(0, 500)
    dudraw.set_y_scale(0, 500)

    # Making sure the entered parameters aren't too big by making them smaller regardless
    if w > 1:
        w = w / 10
    if h > 1:
        h = h / 50

    # Creating the 2 velocity variables for the animations
    rec_velo = .35
    rec_velo2 = .35
 
    # Creating the positionable and scalable variables for the two dudraw objects
    x = x + 75 * w
    y = y + 75 * h
    w = w * 5
    h = h * 25
    
    # Starting a infinite while loop 
    while True:
        if dudraw.has_next_key_typed():
            key = dudraw.next_key_typed()
            # If the key 'g' is pressed the background color will randomly change
            if key == 'g':
                # Clearing the background with random rgb values
                dudraw.clear_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Setting color to orange
        dudraw.set_pen_color(dudraw.ORANGE)
        # Setting width to 5
        dudraw.set_pen_width(5)
        # Drawing larger orange ellipse
        dudraw.filled_ellipse(x + 150, y + 50, w * 5, h * 2.5)

        # Setting color to blue
        dudraw.set_pen_color(dudraw.BLUE)
        # Setting width to 5
        dudraw.set_pen_width(5)
        # Drawing smaller blue ellipse
        dudraw.filled_ellipse(x, y, w, h)

        # Displaying the animation 
        dudraw.show(1)

        # Creating the velocity change for both objects
        y = y + rec_velo
        x = x + rec_velo
        
        y2 = y + rec_velo2
        x2 = x + rec_velo2

        # Checking if the object is close to the border and having it bounce off whatever edge its on

        if y > 475:
            rec_velo = -rec_velo
        if y < 25:
            rec_velo = .35

        if x > 475:
            rec_velo = -rec_velo
        if x < 25:
            rec_velo = .35

    
        if y2 > 475:
            rec_velo2 = -rec_velo
        if y2 < 25:
            rec_velo = .35

        if x2 > 475:
            rec_velo = -rec_velo
        if x2 < 25:
            rec_velo = .35
        
# Calling the function 
my_animation(25, 25, 25, 250)