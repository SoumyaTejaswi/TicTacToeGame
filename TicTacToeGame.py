import random
board=["-","-","-",
       "-","-","-"
       ,"-","-","-"] #global variable.list called board which is 3 by 3 square of dashes
currentPlayer="X" #ANOTHER GLOBAL PLAYER CURRENT PLAY .START VERY GAME WITH PLAYER X
winner=None
gameRunning=True #gamerunning will control the loop

#Printing the game board
def printBoard(board): #printing each row of the board
    print(board[0] + "|" + board[1] + "|"+ board[2])
    print("------")
    print(board[3] + "|" + board[4] + "|"+ board[5])
    print("------")
    print(board[6] + "|" + board[7] + "|"+ board[8])
    print("------")
printBoard(board)

#take player 1 input:Ask the user to select the number from 1 to 9 and each number will correspind to the board
def playerInput(board):
    inp=int(input("Enter a number 1-9:")) #python lib to get the input.it resturns a string value so to work with indexes we need the return type as int
    if inp>=1 and inp <=9 and board[inp-1]=="-": #i first two exp input is valid number 1-9.third check to see that no player has gone there yet. 
        board[inp-1]=currentPlayer #set that pos equal to current player.
    else:
        print("Oops!Another player is already in that spot!")

#check to see if it is a win or tie
        #3 ways to win :horizontally,up and dow and diagnolly
#1 horizontal
def checkHorizontal(board):
    global winner
    if board[0]==board[1]==board[2] and board[1]!="-":
        winner=board[0]
        return True
    elif board[3]==board[4]==board[5] and board[3]!="-":
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!="-":
        winner=board[6]
        return True
#2 Up and down
def checkRow(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!="-":
        winner=board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1]!="-":
        winner=board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2]!="-":
        winner=board[2]
        return True
#3 Daignolly
def checkDiagnol(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!="-":
        winner=board[0]
        return True
    elif board[2]==board[4]==board[6] and board[1]!="-":
        winner=board[2]
        return True
#To check if there is a tie
def checkTie(board):
    if "-" not in board:
        printBoard(board)
        print("It is a tie")
        gameRunning=False
def checforwin():
    if checkDiagnol(board) or checkHorizontal(board) or checkRow(board):
        print(f"The winner is {winner}")

#switch the player 0
def switchPlayer() :
    global currentPlayer
    if currentPlayer=="X":
        currentPlayer="O"
    else:
        currentPlayer="X"

#Playing with the computer
def computer(board):
    while currentPlayer=="O":
        pos= random.randint(0,8) #generate random module to generate random number
        if board[pos]=="-":
            board[pos]="O"
            switchPlayer()

#check if it is a win or tie again:
while gameRunning:
    printBoard(board)
    playerInput(board)
    checforwin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checforwin()
    checkTie(board)

