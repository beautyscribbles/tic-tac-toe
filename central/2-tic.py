import random
# A 4-by-4 input tictactoe game

# Initialize the board with empty spaces
board = [' ' for _ in range(16)]


# Function to display the board
def display_board():
    print()
    print(f'{board[0]} | {board[1]} | {board[2]} | {board[3]}')
    print('-'*13)
    print(f'{board[4]} | {board[5]} | {board[6]} | {board[7]}')
    print('-'*13)
    print(f'{board[8]} | {board[9]} | {board[10]} | {board[11]}')
    print('-'*13)
    print(f'{board[12]} | {board[13]} | {board[14]} | {board[15]}')
    print()


# Function to check if the board is full
def is_board_full():
    return ' ' not in board

# Function to check if a player has won
def check_for_win(player):

    # Check rows
    for i in range(0, 13, 4):
        if board[i] == board[i+1] == board[i+2] == board[i+3] == player:
            return True
    
    # Check columns
    for i in range(4):
        if board[i] == board[i+4] == board[i+8] == board[i+12] == player:
            return True
    
    # Check diagonals
    if board[0] == board[5] == board[10] == board[15] == player:
        return True
    if board[3] == board[6] == board[9] == board[12] == player:
        return True
    return False

# Function for the computer's turn
def computer_move():
    global board
    # Check for a winning move
    for i in range(0, 16):
        if board[i] == ' ':
            board[i] = 'O'
            if check_for_win('O'):
                return
            board[i] = ' '
    # Check for a blocking move
    for i in range(0, 16):
        if board[i] == ' ':
            board[i] = 'X'
            if check_for_win('X'):
                board[i] = 'O'
                return
            board[i] = ' '
    # Make a random move
    while True:
        i = random.randrange(16)
        if board[i] == ' ':
            board[i] = 'O'
            return

# Function for a player's turn
def player_move():
    global board
    while True:
        move = input('Enter your move (1-16): ')
        try:
            move = int(move) - 1
            if move < 0 or move > 15:
                print('Invalid move, please try again.')
            elif board[move] != ' ':
                print('That space is already occupied, please try again.')
            else:
                board[move] = 'X'
                break
        except ValueError:
            print('Invalid move, please try again.')

# Main game loop
while True:
    display_board()
    player_move()
    if check_for_win('X'):
        print('Congratulations! You win!')
        break
    if is_board_full():
        print('The game is a draw.')
        break
    computer_move()
    if check_for_win('O'):
        display_board()
        print

