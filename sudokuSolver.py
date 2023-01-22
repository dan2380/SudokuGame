from __future__ import print_function
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

"""
func: print_board(board)
will print the board in readable format
returns: nothing
"""


def print_board(board):

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


"""
func: find_empty(board)
returns: row, col of next empty spot on the board, denoted by 0
"""


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)  # return (row, col )


"""
func: isValid(board, num, pos):
check horizontal, vertical, and in box to see if that number exists, if it does return False
return: boolean value on if placing a set number in a specific position is valid
"""


def isValid(board, num, pos):

    # check row
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # check col
    for j in range(len(board)):
        if board[pos[0]][j] == num and pos[1] != j:
            return False

    # check 3x3 matrix
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3+3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


"""
func: solve(board)
solves the board using backtracking and recursively finds the next available solution for each 
sudoku square and backtracks when solution fails 
returns: nothing
"""


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if isValid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


print("Initial Board")
print_board(board)
solve(board)
print("-----------------------------------")
print("Solved Board")
print_board(board)
