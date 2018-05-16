import random

game_over = False

board = [
[" "," "," "],
[" "," "," "],
[" "," "," "]
]



def drawBoard():

    print(' ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print('-----------')
    print(' ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
    print('-----------')
    print(' ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])

def play_mark(player, player_row, player_colone ):
    if player_row >=3 or player_colone >=3 :
        print("pick a number between 1-3 for the row and colone")
        return False
    elif board[player_row][player_colone] == " ":
        board[player_row][player_colone]= player
        return True
    else:
        print("space is not empty")
        return False




def winner(name):
    if ((board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != " ") or
     (board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != " ") or
     (board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != " ") or
     (board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != " ") or
     (board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != " ") or 
     (board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != " ") or
     (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " ") or
     (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != " ") ):

        print ("GAME OVER")
        print (name + " WIN")
        return True
    elif " " not in board[0] and " " not in board[1] and " " not in board[2]:
        print ("GAME OVER")
        print (" TIDE")
        return True

    else: 
        return False

def game_loop():
    player = "X"
    name = " "
    player1 = input("player1 enter your name ")
    player2 = input("player2 enter your name ")
    print ("Welcome " + player1 + " and " + player2 + " to Tic Tac Toe! GOOD LUCK")
    print (player1 + " you are X")
    print (player2 + " you are O" )
    while not winner(name):
        if player =='X':
            name = player1
        else:
            name = player2

        player_row = input(name +" pick a row ").lower().strip()
        player_colone = input(name +" pick a colone ").lower().strip()

        if player_row == "quit" or player_colone == "quit" :
            print(" you quit. ")
            print(" GAME OVER")
            return
        elif player_row == " " or player_colone == " " :
            print (" you need to inter a row and colone")

        else :
            if play_mark (player, int(player_row)-1, int(player_colone)-1) :
                drawBoard();
                if player == "X" :
                    player = "O"
                else:
                    player = "X"

game_loop()
