import torch
from torch.nn import Linear
import torch.nn.functional as F
from torch_geometric.nn import GINConv
import torch.nn as nn

class GIN(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, batch_size, num_layers=5):
        super(GIN, self).__init__()
        self.batch_size = batch_size
        self.conv1 = GINConv(nn.Sequential(nn.Linear(input_dim, hidden_dim),
                                           nn.ReLU(),
                                           nn.Linear(hidden_dim, hidden_dim)))
        self.convs = nn.ModuleList()
        for _ in range(num_layers - 1):
            self.convs.append(GINConv(nn.Sequential(nn.Linear(hidden_dim, hidden_dim),
                                                    nn.ReLU(),
                                                    nn.Linear(hidden_dim, hidden_dim))))
        self.fc = nn.Linear(hidden_dim*5, output_dim)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = F.relu(self.conv1(x, edge_index))
        for conv in self.convs:
            x = F.relu(conv(x, edge_index))
        x = x.view(self.batch_size, -1, x.shape[-1])
        x = x.view(self.batch_size, -1)
        x = self.fc(x)
        return x
