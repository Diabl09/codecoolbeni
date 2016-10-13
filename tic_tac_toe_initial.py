import os

def print_board(board):
    for i in range(3):
        print(" ", end="")
        for j in range(3):
            #print X or O, after user gave input
            if 0 < move_count:
                if board[i*3+j] == 1:
                    print('X', end="")
                elif board[i*3+j] == 0:
                    print('O', end="")
                else: 
                    print(' ', end="")
            #print board with instruction numbers
            else:
                print(board[i*3+j], end="") 
            #print sepatation wall
            if j != 2:
                print(" | ", end="")
        #print sepatation wall
        if i != 2:
            print("\n""-----------")
    print("\n")

def print_instruction():
	print("You can use the folling numbers to make your move:\n")
	print_board([1,2,3,4,5,6,7,8,9])

def user_input(player):
    while not win: 
        try: 
            player_input = input("Turn: Player " + player + " - Where would you " +
                        "like to place the " + player + " mark(1-9)? ")
            player_input = int(player_input)
            if player_input >=1 and player_input <= 9 and board[player_input-1] == ' ': 
                return player_input - 1
            else: 
                print("\nThat is not a valid move, please try again.\n")
        except Exception as e:
            print("This is not a valid move, please try again.\n")

def check_win(board):
    
    if board[0] == board[1] and board[0] == board[2] and board[0] != (" "):
        who_the_winner(board)    
    if board[4] == board[3] and board[4] == board[5] and board[4] != (" "):
        who_the_winner(board)
    if board[8] == board[7] and board[8] == board[6] and board[8] != (" "):
        who_the_winner(board)
    if board[0] == board[3] and board[0] == board[6] and board[0] != (" "):
        who_the_winner(board)
    if board[4] == board[1] and board[4] == board[7] and board[4] != (" "):
        who_the_winner(board)
    if board[8] == board[5] and board[8] == board[2] and board[8] != (" "):
        who_the_winner(board)
    if board[0] == board[4] and board[0] == board[8] and board[0] != (" "):
        who_the_winner(board)
    if board[4] == board[2] and board[4] == board[6] and board[4] != (" "):
        who_the_winner(board)

def who_the_winner(board):
    
    winner = ' '
    if board[0] == 0 or board[4] == 0 or board[8] == 0:
        winner = 'playerO'
    elif board[0] == 1 or board[4] == 1 or board[8] == 1:    
        winner = 'playerX'
    
    winner_script(winner)

def no_more_step(board):

    global win

    if board.count(" ") == 0:
        print("There is no winner.")
        win = True

def winner_script(winner):
    
    global win

    if winner == 'playerO':
        print("The winner is O")
    
    elif winner == 'playerX':
        print("The winner is X")
    
    quit()

#main
clear = os.system('cls' if os.name == 'nt' else 'clear')
board = [' '] * 9
move_count = 0
player = 'X'
win = False
print_instruction()

while True:
    no_more_step(board)
    check_win(board)
    move_count += 1
    player_input = user_input(player)

    if move_count % 2 == 0:
        player = 'X'
    else: 
        player = 'O'

    if player == 'O':
        board[player_input] = 1
    else:
        board[player_input] = 0
    print_board(board)
    