# 1. Get the user's name
# 2. Create a valid sudoku grid composed of a CONTAINER, GRID, and TILES (Tiles are inside GRID)    
# 3. Remove 1 inner 2x2 (Henceforth referred to as GRID) tile to enable sliding
# 4. Create a valid killer grid (The one that shows the sums for the valid sudoku grid)
# 5. Randomize the 3 remaining 2x2 tiles position in reference to the outer 2x2 container (Henceforth referred to as CONTAINER)
# 6. Following a set of rules as to not leave the puzzle unsolvable, remove number from the GRIDs
# 7. Display the CONTAINER and GRID to the user, overlap the KILLER GRID on top of the CONTAINER
# 8. Enable the user to slide the GRID tiles
# 8. Get the user's input
# 9. Check if the user's CONTAINER matches the originally generated CONTAINER
# 10. If correct, say YOU WIN, else: do not end the game, the user is able to remove only tiles they have places

"""
Función negra que muestra el inicio de una matriz random
Función para matriz roja que se mueve en el eje vertical (o sea para arriba o para abajo)
Función para matriz azul que se mueve en el eje horizontal (de lados)
Funcion para matriz verde que se mueve en diagonal
1er nivel es de 2 * 2  
"""
import random
from os import remove
from random import randint
from tkinter.messagebox import RETRY

from numpy.matrixlib.defmatrix import matrix


# def read_user_score(): #Function to read the user's score from a file
#     try:
#         #TODO Read the users score from a file
#         return username, score, difficulty
#         pass
#     except FileNotFoundError: #If the file is not found, print the following message
#         print("No save file found")
#
# def store_user_score(f_username, f_score, f_difficulty): #Function to store the user's score in a file
#     try:
#         #TODO Write the user's name and score to the file
#         pass
#     except FileNotFoundError: #If the file is not found, print the following message
#         print("No save file found")

def create_user(): #Function to store the user's score, score is based on a value given to each difficulty divided by time taken to complete the puzzle
    f_name = check_input_validity_str("What is your name? ") #Ask the user for their name
    return f_name #Return the user's name

def check_input_validity_str(f_prompt): #Function to check if any inputted string is valid
    while True: #While loop to keep asking for input until a valid input is given
        try: #Try to convert the input to a string
            f_answer = input(f_prompt)
            if f_answer != "": #If the input is not empty, return the input
                f_answer = f_answer.strip() #Remove any leading or trailing white spaces
                return f_answer #Return the input
            else: #If the input is empty, print the following message
                print("Please enter a non-empty input.")
        except ValueError: #If the input is not a string, print the following message
            print("Invalid input.")

def check_input_validity_int(f_prompt): #Function to check if any inputted integer is valid
    while True: #While loop to keep asking for input until a valid input is given
        try: #Try to convert the input to an integer
            f_answer = int(input(f_prompt))
            if f_answer >= 0: #If the input is greater than or equal to 0, return the input
                return f_answer #Return the input
            else: #If the input is less than 0, print the following message
                print("Please enter a non-negative number.")
        except ValueError: #If the input is not an integer, print the following message
            print("Invalid input. Please enter a valid number.")

def difficulty_choice(): #Function to ask the user to choose a difficulty
    f_difficulty = check_input_validity_int(""" 
What difficulty would you like to play? 
1.Easy 
2.Medium 
""")
    if f_difficulty == 1:
        print("Easy difficulty chosen")
        return 1

    elif f_difficulty == 2:
        print("Medium difficulty chosen")
        return 2

    else:
        print("Please choose a valid difficulty")
        difficulty_choice() #If the user does not choose a valid difficulty, ask them to choose again

# def clock(): #Function to start the clock
#     pass #TODO IMPLEMENT CLOCK
#     return 0 #Placeholder return value


def sudoku_2x2_inner(): #Function to create a valid sudoku grid composed of a CONTAINER, GRID, and TILES (Tiles are inside GRID, GRID is inside CONTAINER)
    matrix_inner = [[random.randint(1, 4) for _ in range(2)] for _ in range(2)]
    matrix_inner = remove_tile(matrix_inner)
    return matrix_inner


def remove_tile(matrix):  # Function to remove 1 inner 2x2 tile to enable sliding
    matrix[random.randint(0, 1), random.randint(0, 1)] = 0


def sudoku_2x2_outer():
    matrix_inner1 = sudoku_2x2_inner()
    matrix_inner2 = sudoku_2x2_inner()
    matrix_inner3 = sudoku_2x2_inner()
    matrix_inner4 = sudoku_2x2_inner()
    matrix_outer = [[matrix_inner1, matrix_inner2], [matrix_inner3, matrix_inner4]]
    return matrix_outer

def randomize_tile(): #Function to randomize the 3 remaining 2x2 tiles position in reference to the outer 2x2 container
    matrix_outer = sudoku_2x2_outer()





def remove_number(): #Function to remove numbers from the GRIDs
    pass #TODO IMPLEMENT REMOVE NUMBER

def display_grid(): #Function to display the CONTAINER and GRID to the user, overlap the KILLER GRID on top of the CONTAINER
    pass #TODO IMPLEMENT DISPLAY GRID, USE A GRAPHICAL INTERFACE LIBRARY

def create_game():
    #This functions combines all the game board creation functions into one and then displays the game board
    sudoku_2x2_outer()
    remove_tile()
    randomize_tile()
    remove_number()
    display_grid()

def slide_tile(): #Function to enable the user to slide the GRID tiles
    pass #TODO IMPLEMENT SLIDE TILE

def get_user_input(): #Function to get the user's input
    pass #TODO IMPLEMENT GET USER INPUT

def check_user_input(): #Function to check if the user's CONTAINER matches the originally generated CONTAINER
    pass #TODO IMPLEMENT CHECK USER INPUT

def win(): #Function to display a message if the user wins
    pass #TODO IMPLEMENT WIN, STORE THE USER'S SCORE

def scoreboard(): #Function to display the scoreboard
    # username, score, difficulty = read_user_score()  # Read the user's score
    pass  # Print the user's score

def menu(): #Function to display the menu
    key_men = check_input_validity_int(""" 
Welcome to crasyudoku!
1. Play
2. Highscores
3. Exit
""")
    if key_men == 1:
        main
    elif key_men == 2:
        scoreboard()
    elif key_men == 3:
        exit()
    else:
        print("Please choose a valid option")
        menu()

# def calculate_score(f_time): #Function to calculate the user's score
#     f_difficulty= difficulty_choice()
#     if f_difficulty == 1: #If the difficulty is easy, the score is 40 divided by the time taken to complete the puzzle
#         f_score = 40/f_time
#     elif f_difficulty == 2: #If the difficulty is medium, the score is 30 divided by the time taken to complete the puzzle
#         f_score = 30/f_time
#     elif f_difficulty == 3: #If the difficulty is sudoku master, the score is 20 divided by the time taken to complete the puzzle
#         f_score = 20/f_time
#     elif f_difficulty == 4: #If the difficulty is impossible, the score is 10 divided by the time taken to complete the puzzle
#         f_score = 10/f_time
#     return f_score #Return the score

def main():
    while True:
        try:
            # Before the game
            username = create_user() #Create the user
            difficulty = difficulty_choice() #Choose the difficulty
            inner_sudoku= sudoku_2x2_inner(difficulty)
            sudoku_2x2_outer(inner_sudoku)


            #Start the game
            # time = clock() #Start the clock
            create_game()

            #Game functions
            get_user_input()
            check_user_input()

            #Win functions
            # score = calculate_score(difficulty, time)  # Calculate the user's score
            # store_user_score(username,score,difficulty) #Store the user's score

            break
        except:
            print("An error occurred, please try again")
            continue


main()
