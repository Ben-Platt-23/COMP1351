""" 
    File Name: platt_project5_optical_illusions.py
    Author: Ben Platt
    Date: 10/06/22
    Course: COMP 1351
    Assignment: Project 4
    Collaborators: None
    Internet Source: None
"""


from dudraw import *
from random import *


def animation():
    """
    Animation function houses the dudraw required statements
    Creating the x and y lists and their speed list
    Main for loop for creating the animation
    """
    # Creating canvas 500 x 500
    dudraw.set_canvas_size(500, 500)
    # Setting the x and y scale for the canvas
    dudraw.set_x_scale(0, 500)
    dudraw.set_y_scale(0, 500)
    # Clearing the background/setting it to white
    dudraw.clear(dudraw.WHITE)

    # Creating the x and y point lists using a for loop and a random number generator 
    x_list = []
    for i in range(100):
        x_list.append(randint(0, 500))
    y_list = []
    for i in range(100):
        y_list.append(randint(0, 500))

    # Creating the speed list for the x and y values 
    speeds = []
    for i in range(100):
        speeds.append(uniform(0.0, 0.03))



    # Starting the for loop for the animation
    for i in range(2):
        # using one for loop as an index for the x and y lists
        for a in range(len(x_list)):
            # setting x and y equal to their respective values in the different lists
            x = x_list[a]
            y = y_list[a]

            # Checking to see if the loop is almost over and setting the second x and y values to index 0 so that the first and last points are connected
            if a == 99:
                x2 = x_list[a-99]
                y2 = y_list[a-99]

            # Setting second x and y values to index a+1 as long as a doesn't equal 99
            if a != 99:
                x2 = x_list[a+1]
                y2 = y_list[a+1]

            # Setting pen color to black
            dudraw.set_pen_color(dudraw.BLACK)
            # Setting pen width to 1
            dudraw.set_pen_width(1)
            # Drawing the line 
            dudraw.line(x, y, x2, y2)
            # Showing for 10 milliseconds
            dudraw.show(10)

            # Changing speeds when needed to prevent any points going off the canvas
            if x >= 500 or x2 >= 500:
                for i in range(len(x_list)):
                    x_list[i] *= -1
            if y >= 500 or y2 >= 500:
                for z in range(len(y_list)):
                    y_list[z] *= -1
            if x <= 0 or x2 <= 0:
                for h in range(len(x_list)):
                    x_list[h] *= -1
            if y <=0 or y2 <= 0:
                for o in range(len(y_list)):
                    y_list[o] *= -1
            

            x_list[a] += speeds[a]
            y_list[a] += speeds[a]

    dudraw.save("/users/benplatt/desktop/platt_image.jpg")
    
     
animation()