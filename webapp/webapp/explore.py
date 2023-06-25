import pandas as pd
from numpy import random
import chess


def get_move(board):
    moves = [mv.uci() for mv in list(board.generate_legal_moves())]
    movindex =random.randint(0, len(moves))
    mov = moves[movindex]
    return mov


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



df = pd.read_csv('../data/games.csv')
