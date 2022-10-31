'''
Filename: platt_project2_height_converter.ipynb 
Author: Ben Platt
Date: 09/19/22
Course: COMP 1351 
Assignment: Height Converter project
Collaborators: None
Internet Source: None
'''    

import math

# Define the height converter function
def height_converter():
    # Asks for the height value from the user and makes sure its set to a float
    height_value = float(input('Please enter your height value in METERS to be converted into feet and inches.'))
    # Checks if height value is less than or equal to 0 and calls the function again if there is an invalid entry
    if height_value <= 0.0:
        print('Invalid entry!')
        height_converter()
    
    # Makes feet variable that takes the height value and multiplies it by 3.28084 to get the amount of feet
    converted_height_feet = height_value * (3.28084)
    # Takes converted height feet and mods it to create a whole number
    converted_height_feet_mod = converted_height_feet % 1
    # Subtracts the above variable from converted height feet to get the whole number
    converted_height_feet_whole = converted_height_feet - converted_height_feet_mod

    # Makes inches variable that takes the height_feet variable and multiplies by 12 to get the amount of inches
    converted_height_inches = converted_height_feet * 12
    # Gets the remainder by dividing inches by 12 to get the leftover inches to display in the final statement
    converted_height_inches_remainder = converted_height_inches % 12
    # Removes the decimal values or simply turns it into a int so the final statement is clearer
    converted_height_inches_remainder = math.trunc(converted_height_inches_remainder)


    # Prints out final statement displaying converstion data
    print('A height of ' + str(height_value) + ' meters is ' + str(converted_height_feet_whole) + ' feet and ' + str(converted_height_inches_remainder) + ' inches.')

height_converter()