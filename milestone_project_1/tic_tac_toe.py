#
# - 2 Players should be able to play the game
# - The board should be printed out every time a player makes a move 
# - You should be able to accept input of the player position and then place a symbol on the board
# - "Numpad" board:
#                   [7,8,9] 
#                   [4,5,6] 
#                   [1,2,3] 
# 
# 1) Select player's chip
# 2) Game loop (accept input and print it into the board)
# 3) Check win/tie
# 4) Ask for replay
# 

empty = "-"
board = ["-","-","-","-","-","-","-","-","-"]

def game():
    tic_tac_toe()

    startAgain = True
    while startAgain:
        user_input = input("Would you like to start again? Yes or No: ")
        if user_input.upper() == "YES":
            # reset the board
            reset()
            # restart the game
            tic_tac_toe()
            startAgain = True
        elif user_input.upper() == "NO":
            startAgain = False
        else:
            print("Selected option was not correct!")

def reset():
    global board
    board = ["-","-","-","-","-","-","-","-","-"]

def tic_tac_toe():
    player_chips = choose_chip()
    player1 = player_chips[0]
    player2 = player_chips[1]
    is_finished = False
    print(f"Player1: {player1} | Player2: {player2}")
    
    display_board(board)
    while is_finished == False:
        # player1 moves
        move(player1, board)
        # first check
        is_finished = position_checker(board, player1, player2)
        if is_finished == False:
            # player2 moves
            move(player2, board)
            # check again
            is_finished = position_checker(board, player1, player2)

def position_checker(board, player1, player2):
    if check(player1, board) == True: 
        print(f"Player {player1} wins!")
        return True
    elif check(player2, board) == True:
        print(f"Player {player2} wins!")
        return True
    elif board_is_full(board) == True:
        print("Game is a tie!")
        return True
    else:
        return False

def check(player, board):
    # check rows
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    elif board[3] == player and board[4] == player and board[5] == player:
        return True
    elif board[6] == player and board[7] == player and board[8] == player:
        return True
    # check cols
    elif board[6] == player and board[3] == player and board[0] == player:
        return True
    elif board[7] == player and board[4] == player and board[1] == player:
        return True
    elif board[8] == player and board[5] == player and board[2] == player:
        return True
    # check diagonals
    elif board[0] == player and board[4] == player and board[8] == player:
        return True
    elif board[6] == player and board[4] == player and board[2] == player:
        return True

def board_is_full(board):
    length = len(list(filter(lambda pos:pos == empty, board)))
    # if length == 0, then the board is full
    if length == 0:
        return True
    else:
        return False

def move(player, board):
    placed = False
    while placed == False:
        value = input(f"Player {player} moves | Choose a position between 1 and 9: ")
        if value.isdigit():
            value = int(value)
            if value in range(1, len(board) + 1) and board[value - 1] == empty:
                print(f"Player {player} has moved | position: {value}")
                # asign chip into board
                board[value - 1] = player
                placed = True
                # display board
                display_board(board)
            else:
                print("Please choose another position.")
        else:
            print("Input is not a number")

def choose_chip():
    done = False
    chips = [] # player1 = pos0, player2 = pos1
    while done == False:
        chip = input("Choose between X or O: ").upper()
        if chip == "X" or chip == "O":
            done = True
            chips = [chip, "X" if chip == "O" else "O"]
        else:
            print("Choosen value was not X or O, please reapeat.")
    return chips

def display_board(board):
    print(f"\n {empty if board[6] == False else board[6]} | {empty if board[7] == False else board[7]} | {empty if board[8] == False else board[8]}")
    print(f" ---------")
    print(f" {empty if board[3] == False else board[3]} | {empty if board[4] == False else board[4]} | {empty if board[5] == False else board[5]}")
    print(f" ---------")
    print(f" {empty if board[0] == False else board[0]} | {empty if board[1] == False else board[1]} | {empty if board[2] == False else board[2]}\n")


game()