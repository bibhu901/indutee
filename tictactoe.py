
import random
# a pattern for displaying the board.

def display_board(board):
    pattern={'a':'        |      |','b':'    {}   |  {}   |   {}   '.format(board[7],board[8],board[9]),'c':'------------------------','d':'    {}   |  {}   |   {}   '.format(board[4],board[5],board[6]),'e':'    {}   |  {}   |   {}   '.format(board[1],board[2],board[3])}
    figure={'f':['a','b','a','c','a','d','a','c','a','e','a']}
    for item in figure['f']:
        print(pattern[item])
        
def player_input():
    marker=''
    while marker!='X' and marker!='O':
        marker=input('Player 1, Choose X or O : ').upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')
        
# A function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.        

def place_marker(board, marker, position):
    print(type(position))
    board[position]=marker   
    
# To check if the player won, using all possible patterns in which player wins.

def win_check(board, mark):
    return board[7]==board[8]==board[9]==mark or board[4]==board[5]==board[6]==mark or board[1]==board[2]==board[3]==mark or board[7]==board[4]==board[1]==mark or board[8]==board[5]==board[2]==mark or board[9]==board[6]==board[3]==mark or board[1]==board[5]==board[9]==mark or board[7]==board[5]==board[3]==mark
 
def choose_first():
    r=random.randint(1,2)
    return 'Player {}'.format(r)

def space_check(board, position):
    return board[position] != 'X' and board[position] != 'O' and board[position] != None
    
def full_board_check(board):
    for item in range(1,10):
        if board[item] != 'X' and board[item] != 'O':
            return False
            break
    else:
        return True
        
def player_choice(board):
    
    while True:
        
        try :
            np=int(input('choose position: '))
            print(type(np))   
        except:
            print('thats not a number.')
            continue
        if np < 1 or np > 9:
            print('enter valid position')
            continue
        if space_check(board, np):
            return np
            break
        else:
            print('space occupied')
            continue
     
def replay():
    ask=input('Do you want to play again?? Y or N : ')
    return ask.upper()== 'Y'
    
# the game below.

print('Welcome to Tic Tac Toe!')

while True:
    (p1,p2)=('','')
    theboard=[' ']*10
    turn = choose_first()
    (p1_marker,p2_marker)=player_input()
    print(turn,' will play first')
    
    start_game=input('Shall we start the game?? : Y or N : ')
    if start_game.upper() == 'Y':
        game_on=True
    else:
        game_on = False

    while game_on:
         #Player 1 Turn
         # the board will be displayed and then marker will be placed in the position the player choses.
        if turn == 'Player 1':            
            display_board(theboard)
            print('player 1 turn')
            position = player_choice(theboard)
            place_marker(theboard, p1_marker, position)
            
            # After each turn it will check if the player won, or its a draw , if neither turn will be changed to player 2.
            
            if win_check(theboard,p1_marker):
                display_board(theboard)
                print('Congratulations!!! Player 1 has won the game.')
                game_on = False
                
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('Its a DRAW')
                    game_on = False
                else:
                    turn = 'Player 2'
                    print('\n'*100)
       
        else:
            # Player2's turn.
            
            display_board(theboard)
            print('player 2 turn')
            position = player_choice(theboard)
            place_marker(theboard, p2_marker, position)
        
            if win_check(theboard,p2_marker):
                display_board(theboard)
                print('Congratulations!!! Player 2 has won the game.')
                game_on = False
            
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('Its a DRAW')
                    game_on = False
                else:
                    turn ='Player 1'
                    print('\n'*100)

    if not replay():
        break    
