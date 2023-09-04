from torch.utils.data import Dataset, DataLoader, Subset
from utilities import *
from numpy.random import randint
import torch.nn as nn
import torch
from model import model

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
        return 400
    
    def __getitem__(self, index):
        
        gameint = randint(1)
        moveint = randint(2)
        board = chess.Board()
        move_listof_game = get_move_list(self.gamesdf['moves'][gameint])
        board_move_list = []
        for i, move in enumerate(move_listof_game):
            board_rep = board_to_rep(board)
            if i%2==1:
                board_rep = board_rep*-1 # Making moving side positive. (essentially indirectly
                    #adding another feature for training - the moving side). The model do not have to guess the moving side.
            move_rep, new_board = move_to_rep(board, move)
            board_move_list.append((board_rep, move_rep))
            # print(board)
            # print('----')
            # board = new_board
        return board_move_list[moveint][0], board_move_list[moveint][1]


data = chess_dataset("data/games.csv")
data_test = Subset(data, range(0, int(len(data)/4)))
data_train = Subset(data, range(int(len(data)/4), int(len(data))))
chess_dataset_loader_train = DataLoader(data_train, batch_size=32, shuffle=True, drop_last=True)
chess_dataset_loader_test = DataLoader(data_test, batch_size=32, shuffle=True, drop_last=True)


mod = model(6)
def trainer(chess_dataset_loader, mod):
    lossfun = nn.CrossEntropyLoss()
    from model import model
    learning_rate = 1e-3
    optimizer = torch.optim.RMSprop(mod.parameters(), lr=learning_rate)
    for inputs, targets in chess_dataset_loader:
        sample = inputs
        out = targets
        loss = lossfun(mod(inputs.float()), targets)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        # print(loss)
    return mod, loss

for epoch in range(12):
    mod.train()
    mod, loss = trainer(chess_dataset_loader_train, mod)
    mod.eval()
    lossfun = nn.CrossEntropyLoss()
    with torch.no_grad():
        for inputs, targets in chess_dataset_loader_test:
            loss = lossfun(mod(inputs.float()), targets)
            print('val loss')
            print(loss)
            
def predictor(board, mod):
    board_rep = board_to_rep(board)
    if board.turn==False:
        board_rep = board_rep*-1
        
    from_, to_ = nn.Softmax()(mod(torch.tensor(board_rep).unsqueeze(0).float())).detach().numpy()[0]
    return from_, to_

# mod(sample[0].unsqueeze(0).float())



