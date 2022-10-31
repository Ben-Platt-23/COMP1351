""" 
    File Name: platt_project7_last_candy.py
    Author: Ben Platt
    Date: 10/26/22
    Course: COMP 1351
    Assignment: Project 7
    Collaborators: None
    Internet Source: None
"""

# Making candy list global so i dont have any scope issues. Candy list represents each box and how much candy is in it. 
global candy_list
candy_list = []
# Going through a loop 6 times and each time setting new a value in the list to 7 eventually leading to 6 boxes of 7 pieces of candy each.
for pile in range(6):
    candy_list.append(7)

# Defining the display function responsible for showing the candy amounts.
def display_game(candy_list):
    # Looping through the length of the candy list. Printing out a little piece of candy for each piece in each box. 
    for candy in range(len(candy_list)):
        display = ('{}'.format(' >()< ' * int(candy_list[candy])))
        print(display)
# Defining the function responsible for asking the players what box and the amount of candy and then it updates the candy list.
def update_candy_list():
    # Making box number global so i dont have any scope issues. 
    global box_number
    box_number = None
    # Creating a loop that will keep asking until it gets a correct response. Checks if the entered number for box number is in the proper range and is actually a number. 
    while box_number not in range(7) or type(box_number) != int:
        box_number = int(input('Please enter a number corresponding to a box of candy (from 1 to 6): '))
        # Exception catching for if selected box is empty already.
        if candy_list[box_number-1] == 0:
            update_candy_list()
        # If the entered number is in the proper range and an int it will break the loop and continue on. 
        if box_number in range(7) and type(box_number) == int:
            break


    # Making candy amount global so i dont have any scope issues. 
    global candy_amount
    candy_amount = None
    # Again creating a loop that checks if the number entered for candy amount is in the proper range and an int. 
    while candy_amount not in range(8) or type(candy_amount) != int:
        candy_amount = int(input('Please enter the amount of candy you would like to remove from the selected box'))
        if candy_amount in range(8) and type(candy_amount) == int:
            break
        
    # Because range starts at 0 the users entered number for box number needs 1 subtracted from it so it actually represents the box they wanted. If the user enters 6 it stays as 6. 
    if box_number == 6:
        box_number = 6
    else:
        box_number = box_number - 1
    # Same situation as above just instead updating the list. 
    if box_number == 6:
        candy_list[5] -= candy_amount
    else:
        candy_list[box_number] -= candy_amount

# Creating the main function housing the game. 
def last_candy():
    # Explains the rules to the players. 
    print("You start out with 6 boxes of candy, and each box contains 7 pieces of candy.\nAt each player’s turn, the player has to remove some candy from one of the boxes.\nThe player can choose the box and the number of pieces of candy to remove from that box.\nThe player who takes the last piece of candy wins the game.")
    
    # Creating two global variables to house both the players names. 
    global player1
    player1 = str(input('Please enter the name of player 1: '))
    global player2
    player2 = str(input('Please enter the name of player 2: '))

    # Creating two global variables representing which players turn it is. 
    global p1turn
    p1turn = True
    global p2turn
    p2turn = False


    # Defining the function that will be called when the game is over to determine the winner. 
    def win_check():
        # Simply checking which turn variable was set to true on the last turn and telling the respective user they won. 
        if p1turn == True:
            print("Congratulations " + str(player1) + " you won!!!")
        elif p2turn == True:
            print("Congratulations " + str(player2) + " you won!!!")
    
    # Checking if the game is over by looking at the sum of candy list. 
    while sum(candy_list) != 0:
        if p1turn == True:
            print("It is " + str(player1) + "'s turn.")
        elif p2turn == True:
            print("It is " + str(player2) + "'s turn.")

        # Shows the candy boxes
        display_game(candy_list)
        # Starts game
        update_candy_list()
        # Checks if game is over and calls win check if it is. 
        if sum(candy_list) == 0:
            win_check()
        else:
            continue
            
        if p1turn == True:
            p2turn = True
            p1turn = False

        elif p2turn == True:
            p1turn = True
            p2turn = False

last_candy()