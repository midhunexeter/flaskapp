import pandas as pd
from numpy import random
import chess
from copy import deepcopy
import itertools
import numpy as np
import re


def get_move(board):
    moves = get_move_list_for_board(board)
    movindex =random.randint(0, len(moves))
    mov = moves[movindex]
    return mov

def get_move_list_for_board(board):
    moves = [mv.uci() for mv in list(board.generate_legal_moves())]
    return moves

def get_board_list_for_board(board):
    moves = [mv.uci() for mv in list(board.generate_legal_moves())]
    boards = [make_a_move(board, mv) for mv in moves]
    return boards

def get_board_list_for_boards(boards):
    board_list= []
    for board in boards:
        board_list.append(get_board_list_for_board(board))
    return itertools.chain(*board_list)

def nestlist(f,x,c):
    # Mathematica's nestlist reproduced
    result = [x]
    for i in range(c):
        x = f(x)
        result.append(x)
    return result


def make_a_move(board, move):
    board_copy = deepcopy(board)
    board_copy.push_uci(move)
    return board_copy

def play_game():
    board = chess.Board()
    random.random
    for i in range(1000):
        mov = get_move(board)
        board.push_uci(mov)
        if board.is_game_over():
            board
            break
    return board





create_rep_slice(board, typ)

df = pd.read_csv("data/games.csv")
df2 = pd.read_csv("data/evals/chessData.csv")