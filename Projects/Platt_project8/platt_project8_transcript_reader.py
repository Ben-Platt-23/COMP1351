""" 
    File Name: platt_project8_transcript_reader.py
    Author: Ben Platt
    Date: 11/09/22
    Course: COMP 1351
    Assignment: Project 8
    Collaborators: None
    Internet Source: None
"""

# Importing the OS package
import os

# Defining the main program
def transcript_reader():
    # Setting the directory for the computer to look for transcripts
    path = "/Users/benplatt/Desktop/School/DU/COMP1351Autumn2022/COMP1351/Projects/Platt_project8"
    # Telling the computer to only look for text files
    ext = ".txt"
    # Setting an empty student file
    student_file = ''
    # Creating a boolean variable for whether the computer found the file or not
    student_found = False
    # Starting a while loop that doesn't stop until it finds a student file
    while student_found == False:
        # Gets first name from user
        first_name = str(input('Please enter students first name (lowercase): '))
        # Gets last name from user
        last_name = str(input('Please enter students last name (lowercase): '))
        # Gets major code from user
        major_code = str(input('Please enter students major code (all caps): '))
        # Creates file name by joining name variables together
        user_file_name = first_name + '_' + last_name + '.txt'
        
        # For loop that looks through the set directory for the student's transcript
        for files in os.listdir(path): 
            if files.endswith(ext):
                if files == user_file_name:
                    student_found = True
                    break
                else:
                    student_found = False
                    continue
    
    # Checks if student has been found
    if student_found == True:
        # Creates emtpy dictionary for student transcript
        student_dict = {}
        # Opens the transcript
        with open('joe_shmo.txt') as f:
            # Reads it line by line
            content = f.readlines()
            # Gets rid of annoying characters
            content = [x.strip() for x in content]
            # Creates an empty index in the student dict
            for i in range(len(content)):
                student_dict[i+1] = []
                # Adds in the students information for each class in a unique key value pair
                for x in range(len(content)):
                    student_dict[x+1] = content[x]
            # Changes the values from a giant string to individual entrys that can be looked up
            for x in range(len(student_dict)):
                student_dict[x+1] = student_dict[x+1].split(",")
    
    # Prints out the students name
    print(str(first_name.capitalize()) + " " + str(last_name.capitalize()))
    # Prints out the students major code
    print(major_code)

    # Creating an emtpy credit hours variable
    credit_hours = 0
    # Going through the student dict and setting all the credit hours to floats instead of strings so they can be tallied
    for x in student_dict:
        student_dict[x][3] = float(student_dict[x][3])
    # Adding all the credit hours together unless the grade is an F
    for z in student_dict:
        if student_dict[z][4] == 'F':
            continue
        else:
            credit_hours += student_dict[z][3]
    
    # Prints out the total university credit hours
    print('University Credit Hours: ' + str(credit_hours))

    # Creates a dict for major specific classes
    major_dict = {}
    # Goes through the key value pairs in student dict and takes out all classes that have the students major code and adds them to the major dict
    for x, y in student_dict.items():
        if y[0] == major_code:
            major_dict[x] = y

    # Creates empty variable for major credit hours
    major_credit_hours = 0
    # Goes through the major dict and tallies up the credit hours again
    for x in major_dict:
        major_credit_hours += major_dict[x][3]
    # Prints out major credit hours
    print('Major credit hours: ' + str(major_credit_hours))
        
    # Creates an emtpy list for the GPA values
    gpa_list = []
    # Creates an emtpy variable for total gpa
    gpa = 0
    count = 0

    # Goes through the student dict and adds all the grades to the GPA list
    for a in student_dict:
        gpa_list.append(student_dict[a][4])

    # Goes through the gpa list and tallies up points based on the grade
    for x in gpa_list:
        if x == 'A+':
            gpa += 4.0
            count += 1
        elif x == 'A':
            gpa += 4.0
            count += 1
        elif x == 'A-':
            gpa += 3.7
            count += 1
        elif x == 'B+':
            gpa += 3.3
            count += 1
        elif x == 'B-':
            gpa += 2.7
            count += 1
        elif x == 'C+':
            gpa += 2.3
            count += 1
        elif x == 'C':
            gpa += 2.0
            count += 1
        elif x == 'C-':
            gpa += 1.7
            count += 1
        elif x == 'D+':
            gpa += 1.3
            count += 1
        elif x == 'D':
            gpa += 1.0
            count += 1
        elif x == 'F':
            gpa += 0
            count += 1
    # Takes the tally and turns it into an average('gpa')
    gpa = gpa / count
    # Prints out total gpa
    print('GPA: ' + str(gpa))

    # Creates emtpy list for major specific grades
    major_gpa_list = []
    # Creates empty variable for major gpa
    major_gpa = 0
    count = 0

    # Goes through the major dict and takes out the grades and adds them to the major gpa list
    for a in major_dict:
        major_gpa_list.append(major_dict[a][4])

    # Goes through the major gpa list and tallies points up based on the grade
    for x in major_gpa_list:
        if x == 'A+':
            major_gpa += 4.0
            count += 1
        elif x == 'A':
            major_gpa += 4.0
            count += 1
        elif x == 'A-':
            major_gpa += 3.7
            count += 1
        elif x == 'B+':
            major_gpa += 3.3
            count += 1
        elif x == 'B-':
            major_gpa += 2.7
            count += 1
        elif x == 'C+':
            major_gpa += 2.3
            count += 1
        elif x == 'C':
            major_gpa += 2.0
            count += 1
        elif x == 'C-':
            major_gpa += 1.7
            count += 1
        elif x == 'D+':
            major_gpa += 1.3
            count += 1
        elif x == 'D':
            major_gpa += 1.0
            count += 1
        elif x == 'F':
            major_gpa += 0
            count += 1
    # Takes the tally and turns it into an average('major gpa')
    major_gpa = major_gpa / count
    # Prints out major gpa
    print(major_gpa)

# Calling the function
transcript_reader()        