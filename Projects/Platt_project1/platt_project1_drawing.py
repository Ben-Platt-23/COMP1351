'''
Author: Ben Platt
Date: 09/13/22
Course: COMP-1351
Assignment: Project 1 Create a Drawing
'''

# Importing the DUdraw package
import dudraw

# Defining my function 'my_drawing' which will run the script to create my image/drawing
def my_drawing():

    # Setting the size of the image and creating a scale
    dudraw.set_canvas_size(500, 500)
    dudraw.set_x_scale(0, 500)
    dudraw.set_y_scale(0, 500)

    # Setting the background to white 
    dudraw.clear(dudraw.WHITE)

    # Drawing all of the light blue circles to create the water
    dudraw.set_pen_color(dudraw.BOOK_LIGHT_BLUE)
    dudraw.set_pen_width(1)
    dudraw.filled_circle(25, 15, 70)
    dudraw.set_pen_color(dudraw.BOOK_LIGHT_BLUE)
    dudraw.set_pen_width(1)
    dudraw.filled_circle(100, 15, 70)
    dudraw.set_pen_color(dudraw.BOOK_LIGHT_BLUE)
    dudraw.set_pen_width(1)
    dudraw.filled_circle(175, 15, 70)
    dudraw.set_pen_color(dudraw.BOOK_LIGHT_BLUE)
    dudraw.set_pen_width(1)
    dudraw.filled_circle(250, 15, 70)
    dudraw.set_pen_color(dudraw.BOOK_LIGHT_BLUE)
    dudraw.set_pen_width(1)
    dudraw.filled_circle(325, 15, 70)
    dudraw.set_pen_color(dudraw.BOOK_LIGHT_BLUE)
    dudraw.set_pen_width(1)
    dudraw.filled_circle(400, 15, 70)
    dudraw.set_pen_color(dudraw.BOOK_LIGHT_BLUE)
    dudraw.set_pen_width(1)
    dudraw.filled_circle(475, 15, 70)

    # Creating the sun in the top right corner
    dudraw.set_pen_color(dudraw.YELLOW)
    dudraw.set_pen_width(1)
    dudraw.filled_circle(500, 500, 150)

    # Drawing a horiztonal line making the boat deck
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.set_pen_width(2)
    dudraw.line(185, 105, 330, 105)

    # Drawing the left side slanted line 
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.set_pen_width(2)
    dudraw.line(185, 105, 220, 70)

    # Drawing the right side slanted line
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.set_pen_width(2)
    dudraw.line(330, 105, 295, 70)

    # Drawing a horizontal line making the bottom of the boat
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.set_pen_width(2)
    dudraw.line(220, 70, 295, 70)

    # Drawing the mast
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.set_pen_width(2)
    dudraw.line(257.5, 105, 257.5, 215)
    # Drawing the flag on the mast
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.set_pen_width(2)
    dudraw.filled_triangle(257.5, 215, 257.5, 185, 220, 200)

    # Showing the drawing
    dudraw.show(10000)

# Calling my function
my_drawing()