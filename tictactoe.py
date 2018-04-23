#Manrique Iriarte
#April 23, 2018
#Python Script to run tic-tac-toe game

import random

#displays board
def Display(board):
    print('\n'*100)
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print("- | - | -")
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print("- | - | -")
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

#gets users input for which mark they will be
def PlayerInput():
    mark = ''
    
    while mark != 'X' and mark != 'O':
        mark = input('Player 1, choose "X" or "O"').upper()
        
    player1 = mark
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
        
    return(player1, player2)

#Places the users mark on the board at the given position
def PlaceMark(board, marker, position):
    if position > 9 or (marker != 'X' and marker != 'x' and marker != 'O' and marker != 'o'):
        pass
    else:
        board[position] = marker.upper()

#Returns true if there was a winner and false if there was not
def Winner(board, mark):
    mark = mark.upper()
    threeinarow = [mark, mark, mark]
    return (board[1:4] == threeinarow or board[4:7] == threeinarow or
            board[7:10] == threeinarow or board[1::4] == threeinarow or
            board[3:8:2] == threeinarow or board[3::3] == threeinarow or
            board[1:8:3] == threeinarow or board[2:9:3] == threeinarow)

#randomly determines who plays first
def ChooseTurn():
    if random.randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'

#Returns true if that given position is free and false if it is not
def Space(board, position):
    return board[position] == ' '

#Returns true if the board is full and false if it is not
def IsFull(board):
    for i in range(1,10):
        if Space(board, i):
            return False
    return True

#Gets the users input for what space they want to put there mark. 
#Also shows a second board with available spaces the user can choose from
def Choice(board, availablePos):
    position = 0
    
    while position not in range(1,10) or not Space(board, position):
        #display available positions
        print(f'{availablePos[7]} | {availablePos[8]} | {availablePos[9]}')
        print("- | - | -")
        print(f'{availablePos[4]} | {availablePos[5]} | {availablePos[6]}')
        print("- | - | -")
        print(f'{availablePos[1]} | {availablePos[2]} | {availablePos[3]}')
        position = int(input("Enter number to place your mark: ")) 
        availablePos[position] = ' '
    
    return position

#Returns true if the user wants to replay the game and false if they do not
def Replay():
    choice = ''
    while choice != 'yes' and choice != 'Yes' and choice != 'no' and choice != 'No':
        choice = input('Play Again?')
    if choice == 'yes' or choice == 'Yes':
        return True
    else:
        return False



while True:
     #initialize my two boards
     available = list(range(0,10))
     board = [' '] * 10
     
     p1, p2 = PlayerInput()
     turn = ChooseTurn()
     
     play = True

     while play: 
        if turn == 'Player 1':
            Display(board)
            print(turn + "'s turn") 
            PlaceMark(board, p1, Choice(board, available))

            if Winner(board, p1):
                Display(board)
                print('Congratulations ' + turn + ', you win! ')
                play = False
            else:
                if IsFull(board):
                    Display(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            Display(board)
            print(turn + "'s turn")
            position = Choice(board, available)
            PlaceMark(board, p2, position)

            if Winner(board, p2):
                Display(board)
                print('Congratulations ' + turn + ', you win! ')
                play = False
            else:
                if IsFull(board):
                    Display(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

     playAgain = Replay()
     
     if not playAgain:
         break
