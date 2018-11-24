# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Jason Hodge
# Created: 2018-11-08
symbol = [ " ", "x", "o" ] 

def printRow(row):
    # initialize output to the left border
    output = "|"
    # for each square in the row...
    for cell in row:
        # add to output the symbol for this square followed by a border
        output += " " + symbol[cell] + "|"
    # print the completed output for this row
    print(output)
    pass

def printBoard(board):
    # print the top border
    # for each row in the board...
        # print the row
        # print the next border
#matrix = [ [0,1],
#          [2,3],
#          [4,5],
#          [6,7],
#          [8,9] ]

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    pass

def markBoard(board, row, col, player):
    # check to see whether the desired square is blank
       # if so, set it to the player number
#   if square blank():
#       input("Row, Column")
    def create_3n_matrix(n):
        return [[[None for x in range(n)] for x in range(n)] for x in range(n)]

    pass

def getPlayerMove():
    input("Enter a row number between 1 & 9")
    input("Enter a column number between 1 & 9")# prompt the user separately for the row and column numbers
    return (0,0) # then return that row and column instead of (0,0)

def hasBlanks(board):
    # for each row in the board...
       # for each square in the row...
          # check whether the square is blank
             # if so, return True
    return True # if no square is blank, return False

def main():
    board = [None] + list(range(1, 10)) # TODO replace this with a three-by-three matrix of zeros
    player = 1
    getPlayerMove()
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board,row,col,player)
        player = player % 2 + 1 # switch player for next turn
main()
