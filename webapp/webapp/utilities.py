import itertools
import re
from copy import deepcopy
import chess
import numpy as np
import pandas as pd
from numpy import random


def board_to_rep(board):
    pieces = ['p', 'r', 'n', 'b', 'q', 'k']
    layers = []
    for piece in pieces:
        layers.append(create_rep_slice(board, piece))
    board_rep = np.stack(layers)
    return board_rep


def create_rep_slice(board, typ):

    if typ != typ.islower():
        Warning('Provide lower case letter')
        typ = typ.lower()

    s = str(board)
    s = re.sub(f'[^{typ}{typ.upper()} \n]', '.', s)
    s = re.sub(f'{typ}', '-1', s)
    s = re.sub(f'{typ.upper()}', '1', s)
    s = re.sub(f'\.', '0', s)
    
    mat = []
    
    for row in s.split('\n'):
        row = row.split(' ')
        row = [int(x) for x in row]
        mat.append(row)
    
    return np.array(mat)



def move_to_rep(move):
    board.push_san(move).uci()
    move = board.pop()

    from_output_layer = np.zeros((8, 8))
    from_row = 8 - int(move[1])
    from_column = letter_to_num(move[0])
    from_output_layer[from_row, from_column] = 1

    to_output_layer = np.zeros((8, 8))
    to_row = 8 - int(move[3])
    to_column = letter_to_num(move[2])
    to_output_layer[from_row, from_column] = 1

    return np.stack([from_output_layer, to_output_layer])


def letter_to_num(letter):

    num = ord(letter)-96

    return num

def get_move_list(moves):
    re.sub('\d*\.', '', moves).split(' ')[:-1]