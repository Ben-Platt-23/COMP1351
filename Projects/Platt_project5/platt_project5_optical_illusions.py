""" 
    File Name: platt_project5_optical_illusions.py
    Author: Ben Platt
    Date: 10/13/22
    Course: COMP 1351
    Assignment: Project 5
    Collaborators: None
    Internet Source: None
"""
import dudraw

# Setting DUDraw parameters
dudraw.set_canvas_size(500, 500)
dudraw.set_x_scale(0, 500)
dudraw.set_y_scale(0, 500)
# Setting background to blue
dudraw.clear(dudraw.BLUE)

# Creating the gray border
dudraw.set_pen_color(dudraw.GRAY)
dudraw.set_pen_width(7.5)
dudraw.rectangle(250, 250, 250, 250)

def lines():
    '''
    Function for creating the horizontal and vertical lines
    Variables below are the base values for the lines
    '''
    
    x0 = 0
    y0 = 500
    x1 = 500
    y1 = 500

    x01 = 100
    y01 = 500
    x11 = 100
    y11 = 0
    # These two for loops create 4 vertical and 4 horizontal gray lines on the canvas
    for a in range(4):
        for b in range(5):
            dudraw.set_pen_color(dudraw.GRAY)
            dudraw.set_pen_width(5)
            dudraw.line(x0, y0, x1, y1)
            y0 = y0 - 100
            y1 = y1 - 100
        dudraw.set_pen_color(dudraw.GRAY)
        dudraw.set_pen_width(5)
        dudraw.line(x01, y01, x11, y11)
        x01 = x01 + 100
        x11 = x11 + 100

def circles():
    '''
    Function for creating the small white circles at each corner on the inside of the canvas
    Variables below are the base values for the circles
    '''
    cx = 100
    cy = 400
    cr = 10

    # These two for loops draw 4 white circles then step down a row and continue until there are 4 rows and 4 columns of white circles 
    for a in range(4):
        for b in range(1):
            dudraw.set_pen_color(dudraw.WHITE)
            dudraw.set_pen_width(1)
            dudraw.filled_circle(cx, cy, cr)
            dudraw.filled_circle(cx + 100, cy, cr)
            dudraw.filled_circle(cx + 200, cy, cr)
            dudraw.filled_circle(cx + 300, cy, cr)
        cy = cy - 100

# Calling the two functions
lines()
circles()

# Displaying the drawing
dudraw.show()
