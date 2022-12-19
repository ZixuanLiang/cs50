"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_X, count_O = 0, 0
    for line in board:
        for cell in line:
            count_X += (cell == X)
            count_O += (cell == O)
    return X if count_O == count_X else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.append((i,j))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result_board = copy.deepcopy(board)
    i, j = action
    if result_board[i][j] == EMPTY:
        result_board[i][j] = player(board)
    else:
        raise Exception('not a valid action')
    return result_board

def isfull(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] != EMPTY:
            return board[i][0]
        if (board[0][i] == board[1][i] == board[2][i]) and board[0][i] != EMPTY:
            return board[0][i]
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != EMPTY:
        return board[0][0]
    if (board[0][2] == board[1][1] == board[2][0]) and board[0][2] != EMPTY:
        return board[0][2] 
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return (winner(board) != None) or isfull(board)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def min_value(board, pre_min):
    v = 2
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action), v))
        if v < pre_min:
            return v
    return v

def max_value(board, pre_max):
    v = -2
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action), v))
        if v > pre_max:
            return v
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    optimal_action = None
    all_actions = actions(board)
    if player(board) == X: # maximize the value
        v = -2
        for action in all_actions:
            min = min_value(result(board, action), v)
            if  min > v:
                v = min
                optimal_action = action
    else: # O tries to minimize the value
        v = 2
        for action in all_actions:
            max = max_value(result(board, action), v)
            if max < v:
                v = max
                optimal_action = action
    return optimal_action

