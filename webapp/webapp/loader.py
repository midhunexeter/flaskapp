from torch.utils.data import Dataset, DataLoader, Subset
from utilities import *
from numpy.random import randint
import torch.nn as nn
import torch
# board = chess.Board()
# rep = board_to_rep(board)
# df = pd.read_csv("data/games.csv")
# df2 = pd.read_csv("data/evals/chessData.csv")
 # Obtain moves of a particular game  
class chess_dataset(Dataset):
    
    def __init__(self, path = "data/games.csv"):
        self.path = path
        self.gamesdf = pd.read_csv(self.path)
        
    def __len__(self):
        return 4000
    
    def __getitem__(self, index):
        
        gameint = randint(1)
        moveint = randint(2)
        board = chess.Board()
        move_listof_game = get_move_list(self.gamesdf['moves'][gameint])
        board_move_list = []
        for i, move in enumerate(move_listof_game):
            board_rep = board_to_rep(board)
            if i%2==1:
                board_rep = board_rep*-1
            move_rep, new_board = move_to_rep(board, move)
            board_move_list.append((board_rep, move_rep))
            # print(board)
            # print('----')
            # board = new_board
        return board_move_list[moveint][0], board_move_list[moveint][1]


data_train = chess_dataset("data/games.csv")
chess_dataset_loader = DataLoader(data_train, batch_size=32, shuffle=True, drop_last=True)

lossfun = nn.CrossEntropyLoss()
from model import model
mod = model(6)
learning_rate = 1e-3
optimizer = torch.optim.RMSprop(mod.parameters(), lr=learning_rate)

for epoch in range(2):
    for inputs, targets in chess_dataset_loader:
        sample = inputs
        out = targets
        loss = lossfun(mod(input.float()), targets)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        print(loss)



# mod(sample[0].unsqueeze(0).float())



