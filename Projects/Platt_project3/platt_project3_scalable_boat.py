""" 
    File Name: platt_project3_scalable_boat.py
    Author: Ben Platt
    Date: 09/30/22
    Course: COMP 1351
    Assignment: Project 3
    Collaborators: None
    Internet Source: None
"""

import dudraw

# Defining my function 'my_drawing' which will run the script to create my image/drawing
def my_drawing(x:float, y:float, w:float, h:float):
    """
    Draws a little boat on the water with the sun in the sky

    :param float x: x position of the lower left corner of the wagon
    :param float y: y position of the lower left corner of the wagon
    :param w: width of the wagon
    :param h: height of the wagon
    """
    
    if w > 1:
        w = w / 500
    if h > 1:
        h = h / 500


    # Drawing the water
    # Setting pen color to light blue
    dudraw.set_pen_color(dudraw.BOOK_LIGHT_BLUE)
    # Setting pen width to 2
    dudraw.set_pen_width(2)
    # Drawing a large blue rectangle to act as water
    dudraw.filled_rectangle(x + 250 * w, y + 0 * h, 250 * w, 100 * h)

    # Drawing the sun 
    # Setting the pen color to yellow
    dudraw.set_pen_color(dudraw.YELLOW)
    # Setting the pen width to 1
    dudraw.set_pen_width(1)
    # Drawing a large yellow circle to act as the sun
    dudraw.filled_ellipse(x + 500 * w, y + 500 * h, 50 * w, 50 * h)

    # Drawing the boat
    # Setting the pen color to black
    dudraw.set_pen_color(dudraw.BLACK)
    # Setting the pen width to 2
    dudraw.set_pen_width(2)
    # Drawing the boat
    dudraw.line(x + 185 * w, y + 105 * h, x + 330 * w, y + 105 * h) 
    dudraw.line(x + 185 * w, y + 105 * h, x + 220 * w, y + 70 * h)
    dudraw.line(x + 330 * w, y + 105 * h, x + 295 * w, y + 70 * h)
    dudraw.line(x + 220 * w, y + 70 * h, x + 295 * w, y + 70 * h)
    dudraw.line(x + 257.5 * w, y + 105 * h, x + 257.5 * w, y + 215 * h)
    dudraw.filled_triangle(x + 257.5 * w, y + 215 * h, x + 257.5 * w, y + 185 * h, x + 220 * w, y + 200 * h)


dudraw.set_canvas_size(500, 500)
dudraw.set_x_scale(0, 500)
dudraw.set_y_scale(0, 500)
dudraw.set_pen_color(dudraw.LIGHT_GRAY)
dudraw.filled_rectangle(0, 0, 500, 500)

my_drawing(25, 25, 225, 225)
my_drawing(25, 375, 200, 50)
my_drawing(375, 275, 50, 200)
my_drawing(375, 125, 50, 50)

dudraw.show(float('inf'))