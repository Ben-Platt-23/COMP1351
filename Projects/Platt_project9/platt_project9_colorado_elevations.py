""" 
    File Name: platt_project9_colorado_elevations.py
    Author: Ben Platt
    Date: 11/18/22
    Course: COMP 1351
    Assignment: Project 7
    Collaborators: Dr. Stevens in class demonstration and slack code
    Internet Source: None
"""

# Importing du draw
import dudraw

# creating an empty list for the elevation values
elevations_txt = open('CO_elevations_feet.txt')
elevations_list = []

for line in elevations_txt:
    lines = line.split()
    values = [int(i) for i in lines]
    elevations_list.append(values)


# Displaying the max elevation 
max_value = 0
for row in elevations_list:
    for value in row:
        if value > max_value:
            max_value = value
        else:
            continue
print(max_value)

# This reverses the elevations list
for i in range(len(elevations_list)):
    elevations_list[i]=elevations_list[i][::-1]

# Creating two variables, one for rows that would just the length of the whole list,
# and cols which is the length of one internal lists in the 2D list
rows=len(elevations_list)
cols=len(elevations_list[0])

# Setting canvas size to exactly the amount of rows and columns
dudraw.set_canvas_size(cols, rows)

# setting the scale also to be able to hold one point for each elevation 
dudraw.set_x_scale(0,cols-1)
dudraw.set_y_scale(0,rows-1)

# Clearing the canvas for the image
dudraw.clear()

# Starting a while loop that encompasses the animation
while True:
    # Goes through each row
    for i in range(rows):
            # Goes through each value in the row
            for j in range(cols):
                # Setting the proper grayscale intensity for each dot using this equation 
                color_val = int((elevations_list[i][j]) / 250000 * 255)

                # Setting the pen color using the rgb function and inputting the same RGB value for each parameter
                dudraw.set_pen_color_rgb(color_val, color_val, color_val)

                # Drawing the points, using j and i as x-cords
                dudraw.filled_square(j, i, 1)
    

    # Checks if the mouse has been pressed
    if dudraw.mouse_pressed():
        # If it has then it changes the pen color to white
        dudraw.set_pen_color(dudraw.WHITE)

        # Setting i and j to a rounded version of whatever the x,y points are that the user clicked on
        i=int(dudraw.mouse_y())
        j=int(dudraw.mouse_x())

        # Displaying the elevation in the bottom right after a click
        dudraw.text(485, 25, str(elevations_list[i][j]))
        # Telling the user what the exact location of the elevation value in the elevations list 
        dudraw.text(j,i,f'You clicked on pixel row {i} and column {j}')

    # Showing the animation 
    dudraw.show(100)