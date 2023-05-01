import pygame
from random import randint



# Hallowwwwwwwwwwwwwwwww

board = [[0 for j in range(9)] for i in range(9)]

# Initializes the board state 
def initBoard(board):
    for i in range(9):
        for j in range(9):
            board[i][j] = randint(0,9)

initBoard(board)
print(board)