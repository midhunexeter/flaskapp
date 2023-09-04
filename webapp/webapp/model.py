import torch.nn as nn
import torch
class model(nn.Module):
    
    def __init__(self, hidden_size) -> None:
        super(model, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=6, out_channels=6,kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(in_channels=6, out_channels=6, kernel_size=3, stride=1, padding=1)
        self.convout = nn.Conv2d(in_channels=6, out_channels=2, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(hidden_size)
        self.bn2 = nn.BatchNorm2d(hidden_size)
        self.activation1 = nn.SELU()
        self.activation2 = nn.SELU()
        
    def forward(self, x):
        x_input = torch.clone(x)
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.activation1(x)
        x = self.conv2(x)
        x= self.bn2(x)
        x = x + x_input
        x = self.activation2(x)
        x = self.convout(x)
        return x
    
    
        
        