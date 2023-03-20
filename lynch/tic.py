#Player vs Player

board = [ ["" for  _ in range(3)] ]

def tiv_board():
    print(" 0 1 2")
    for i, row in enumerate(board):
        print(i, " ".join(row))

def move_acc(player):
    while True:
        col  = input(f"{player}, enter column: ")
        row = input(f"{player}, enter row: ") 
        if col.isdigit() and row.isdigit():
            col, row = int(col), int(row)
            if 0 <= col < 5 and 0 <= row < 5:
                #The column and row must be less than or equal to 5 
                if board[row][col] == " ":
                    board[row][col] = player
                    return
                else:
                    print("That space is already occupied. Try again")
            else:
                print("Invalid move. Try again.")
        else :
                print("Invalid input. Try again.")

def has_winner():
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] == row[3] == row[5] and row[0] != " ":
            return True
        # Check columns
        for col in range(5):
            if board[0][col == board][1][col] == board[2][col] == board[3][col] == board[4][col] and board[0][col] != " ":
                return True
        # Check diagonals
        if board[0][0] == board [1][1] == board[2][2] == board[3][3] == board[4][4] and board[0][0] != " ":
            return True
        if board[2][0] == board[1][1] == board[0][1] == board[1][0] == board[0][2] == board[2][0] == board[3][0] == board[0][3] and board[3][0] != " ":
            return True
        return False
