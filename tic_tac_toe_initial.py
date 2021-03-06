import os

def print_board(board):
    for i in range(3):
        print(' ', end='')
        for j in range(3):
            #print X or O, after user gave input
            if -1 < move_count:
                if board[i*3+j] == 1:
                    print(playerX, end='')
                elif board[i*3+j] == 0:
                    print(playerO, end='')
                else: 
                    print(' ', end='')
            #print board with instruction numbers
            else:
                print(board[i*3+j], end='') 
            #print walls
            if j != 2:
                print(' | ', end='')
        #print walls
        if i != 2:
            print('\n''-----------')
    print('\n')

def print_instruction():
	print('You can use the folling numbers to make your move:\n')
	print_board([1,2,3,4,5,6,7,8,9])

# provide input from user, input check
# exit condition
def user_input(player):
    while True: 
        try: 
            player_input = input('Turn: Player ' + player + ' - Where would you ' +
                        'like to place the ' + player + ' mark(1-9)? ')
            print('\n')
            if player_input == 'exit':
                quit()
            player_input = int(player_input)
            if player_input >=1 and player_input <= 9 and board[player_input-1] == ' ': 
                return player_input - 1
            else: 
                print('\n\033[1;31mThat is not a valid move, please try again.\033[1;m\n')
        except:
            print('\033[1;31mThis is not a valid move, please try again.\033[1;m\n')

# win and winner check functions
def check_win(board):
    if board[0] == board[1] and board[0] == board[2] and board[0] != (' '):
       who_the_winner_0(board)    
    if board[4] == board[3] and board[4] == board[5] and board[4] != (' '):
        who_the_winner_4(board)
    if board[8] == board[7] and board[8] == board[6] and board[8] != (' '):
        who_the_winner_8(board)
    if board[0] == board[3] and board[0] == board[6] and board[0] != (' '):
        who_the_winner_0(board)
    if board[4] == board[1] and board[4] == board[7] and board[4] != (' '):
        who_the_winner_4(board)
    if board[8] == board[5] and board[8] == board[2] and board[8] != (' '):
        who_the_winner_8(board)
    if board[0] == board[4] and board[0] == board[8] and board[0] != (' '):
       who_the_winner_0(board)
    if board[4] == board[2] and board[4] == board[6] and board[4] != (' '):
        who_the_winner_4(board)

def who_the_winner_0(board):
    global winner
    if board[0] == 0:
        winner = playerO
    elif board[0] == 1:    
        winner = playerX
    
    winner_script(winner)

def who_the_winner_4(board):
    global winner
    if board[4] == 0:
        winner = playerO
    elif board[4] == 1:    
        winner = playerX
    
    winner_script(winner)

def who_the_winner_8(board):
    global winner
    if board[8] == 0:
        winner = playerO
    elif board[8] == 1:    
        winner = playerX
    
    winner_script(winner)

# End functions
def winner_script(winner):
    if winner == playerO:
        print('\033[1;33mThe winner is O\033[1;m')
        
    elif winner == playerX:
        print('\033[1;36mThe winner is X\033[1;m')
    restart_f()

def no_more_step(board):
    if board.count(' ') == 0:
        print('There is no winner.')
        restart_f()

# restart
def restart_f():
    start_again = input('If you want to start again type y? \n')    
    if start_again == 'y':
        main()
    else:
        quit()

def main():
    global board
    global move_count
    global playerX
    global playerO
    while True:
        # variables
        clear = os.system('cls' if os.name == 'nt' else 'clear')
        board = [' '] * 9
        move_count = -1
        playerX = '\033[1;36mX\033[1;m'
        playerO = '\033[1;33mO\033[1;m'
        winner = ' '
        print_instruction()

        # input handling, moves counting
        while True:
            no_more_step(board)
            check_win(board)
            move_count += 1

            if move_count % 2 == 0:
                player = playerX
            else: 
                player = playerO
            player_input = user_input(player)

            if player == playerX:
                board[player_input] = 1
            else:
                board[player_input] = 0
            print_board(board)

main()