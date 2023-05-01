import pygame
from random import randint, choices



# Difficulty level can be 1 = Easy, 2 = Medium, 3 = Hard
def weightedRand(difficulty):
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    if difficulty == 1:
        # Easy: 3x more likely for empty tiles to appear
        weights = [3, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    elif difficulty == 2:
        # Medium: 3x more likely for empty tiles to appear
        weights = [5, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    elif difficulty == 3:
        # Hard: 3x more likely for empty tiles to appear
        weights = [9, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    else:
        return None

    return choices(values, weights)[0]

# Initializes the board state based on the given difficulty level
def initBoard(difficulty):
    board = [[0 for j in range(9)] for i in range(9)]

    for i in range(9):
        for j in range(9):
            board[i][j] = weightedRand(difficulty)

    return board

#testBoard = initBoard(2)
#print(testBoard)