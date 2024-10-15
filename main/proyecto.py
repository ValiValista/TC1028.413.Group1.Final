import random
import time
import threading
import os

# Function to validate that the input is an integer and not something else in the menu
def get_valid_input_int(prompt):
    while True:
        try:
            answer = int(input(prompt))
            if answer >= 0:
                return answer
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def initialize_board():
    board = [[0] * 4 for _ in range(4)]  # Create a 4x4 board initialized with zeros
    add_new_tile(board)  # Add the first random number
    add_new_tile(board)  # Add the second random number
    return board

def add_new_tile(board):
    empty_tiles = [(r, c) for r in range(4) for c in range(4) if board[r][c] == 0]  # Find all empty positions recorriendo r y c
    if empty_tiles:
        r, c = random.choice(empty_tiles)  # Place the new tile in a random empty cell
        if random.random() < 0.9: #Genera la probabilidad de que si me da un numero menor a 0.9 (que es el 90%) pondrá un 2 en una línea random
            board[r][c] = 2
        else:
            board[r][c] = 4 #Si es mayor a 0.9 pondrá el numero 4

def print_board(board): #Se usa diccionario para colores ANSI
    color_map = {
        0: "\033[97m",  # White
        2: "\033[92m",  # Green
        4: "\033[94m",  # Blue
        8: "\033[36m",  # Cyan
        16: "\033[95m",  # Magenta
        32: "\033[93m",  # Yellow
        64: "\033[91m",  # Red
        128: "\033[32m",  # Light Green
        256: "\033[33m",  # Light Yellow
        512: "\033[37m",  # Light Cyan
        1024: "\033[35m",  # Light Magenta
        2048: "\033[34m"  # Light Blue
    }
    reset_color = "\033[0m"
    for row in board:
        row_str = ""
        for num in row:
            color = color_map.get(num, "\033[97m")  # Add color
            if num != 0:
                row_str += color + str(num) + "\t" + reset_color  # Add color
            else:
                row_str += ".\t"
        print(row_str)
    print()

def slide_and_combine_row(row):
    new_row = [num for num in row if num != 0]  # Remove zeros
    for i in range(len(new_row) - 1):
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            new_row[i + 1] = 0
    final_row = [num for num in new_row if num != 0]  # Remove zeros again
    final_row += [0] * (4 - len(final_row))  # Add zeros to the end
    return final_row

def move_left(board):
    return [slide_and_combine_row(row) for row in board]

def rotate_board(board):
    return [list(row) for row in zip(*board[::-1])]  # Rotate the board

def move(board, direction):
    for _ in range(direction):
        board = rotate_board(board)
    board = move_left(board)
    for _ in range((4 - direction) % 4):
        board = rotate_board(board)
    return board

def is_game_over(board):
    if any(0 in row for row in board):
        return False
    for r in range(4):
        for c in range(4):
            if (r < 3 and board[r][c] == board[r + 1][c]) or (c < 3 and board[r][c] == board[r][c + 1]):
                return False
    return True

def get_board_sum(board):
    return sum(sum(row) for row in board)  # Calculate the sum of all numbers on the board

def save_to_csv(user_name, score, total_time):
    encabezadoResultados = 'Nombre, Puntaje, Tiempo\n'
    file_path = 'game_scores.csv'
    try:
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write(encabezadoResultados)
        with open(file_path, 'a', newline='') as file:
            resultados = f'{user_name},{score},{total_time}\n'
            file.write(resultados)
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

def get_highest_score():
    highest_score = None
    highest_score_data = None
    try:
        if os.path.exists('game_scores.csv'):
            with open('game_scores.csv', 'r') as file:
                reader = (line.strip().split(',') for line in file)
                next(reader)  # Skip the header
                for row in reader:
                    name, score, time_played = row
                    score = int(score)
                    if highest_score is None or score > highest_score:
                        highest_score = score
                        highest_score_data = (name, score, time_played)
    except FileNotFoundError:
        pass
    return highest_score_data

def play_game_1():
    user_name = input("Please enter your name: ").strip()
    start_time = time.time()  # Start counting time when the game starts
    board = initialize_board()
    while True:
        print_board(board)
        print("Instructions")  # Write clear and precise instructions
        move_input = input(f"\nw: up \ns: down \na: left \nd: right  \n {user_name} Enter a move: ").strip().lower()
        if move_input == "w":
            direction = 3
        elif move_input == "s":
            direction = 1
        elif move_input == "a":
            direction = 0
        elif move_input == "d":
            direction = 2
        else:
            print("Invalid move! Please enter 'w', 'a', 's', or 'd'.")
            continue
        new_board = move(board, direction)
        if new_board != board:
            board = new_board
            add_new_tile(board)
        if is_game_over(board):
            print_board(board)
            end_time = time.time()
            final_time = (end_time - start_time) / 60  # Calculate total game time
            board_sum = get_board_sum(board)  # Get the sum of all numbers
            print(f"Game Over, {user_name}! \nFinal Score: {board_sum} \nTotal Time: {final_time:.2f} minutes")
            save_to_csv(user_name, board_sum, final_time)
            highest_score_data = get_highest_score()
            if highest_score_data:
                name, high_score, time_played = highest_score_data
                if user_name == name and board_sum == high_score:
                    print(f"Congratulations {user_name}! \nYou have the highest score with a score: {high_score} \nwith time of {time_played} minutes.")
                else:
                    print(f"The highest score so far is by {name} \n     Score of {high_score} \n     Time: {time_played:.2f} minutes.")
            break

def get_user_input():
    global move_input
    move_input = input().strip().lower()

def play_game2():
    user_name = input("Please enter your name: ").strip()
    start_time = time.time()  # Start counting time when the game starts
    board = initialize_board()
    global move_input
    while True:
        print_board(board)
        print("Instructions \nw: up \ns: down \na: left \nd: right")  # Write clear and precise instructions
        move_input = None
        input_thread = threading.Thread(target=get_user_input)  # Create a thread for user input
        input_thread.start()
        input_thread.join(timeout=5)  # Wait for user input within 5 seconds
        if move_input is None:  # Check if the user did not enter a move within the time limit
            print("\nTime's up! You took too long to make a move.\nGame Over!\n")
            time.sleep(1)
            break
        if move_input == "w":
            direction = 3
        elif move_input == "s":
            direction = 1
        elif move_input == "a":
            direction = 0
        elif move_input == "d":
            direction = 2
        else:
            print("Invalid move! Please enter 'w', 'a', 's', or 'd'.")
            continue
        new_board = move(board, direction)
        if new_board != board:
            board = new_board
            add_new_tile(board)
        if is_game_over(board):
            print_board(board)
            end_time = time.time()
            final_time = (end_time - start_time) / 60  # Calculate total game time
            board_sum = get_board_sum(board)  # Get the sum of all numbers
            print(f"Game Over, {user_name}! \nFinal Score: {board_sum} \nTotal Time: {final_time:.2f} minutes")
            save_to_csv(user_name, board_sum, final_time)
            highest_score_data = get_highest_score()
            if highest_score_data:
                name, high_score, time_played = highest_score_data
                if user_name == name and board_sum == high_score:
                    print(f"Congratulations {user_name}! \nYou have the highest score with a score: {high_score} \nwith time of {time_played} minutes.")
                else:
                    print(f"The highest score so far is by {name} \n     Score of {high_score} \n     Time: {time_played:.2f} minutes.")
            break

def main():
    while True:
        user_choice = get_valid_input_int(
            """Do you want to play 2048: \n1. No time limit \n2. Time limit (5 seconds for each move) \n \nPress the indicated number: """)
        if user_choice == 1:
            play_game_1()
        elif user_choice == 2:
            play_game2()
        else:
            print("Invalid choice. Please enter 1 or 2.")

main()