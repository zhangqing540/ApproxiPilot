import torch
from torch.nn import Linear
import torch.nn.functional as F
from torch_geometric.nn import TAGConv
import torch.nn as nn
from torch_geometric.utils import add_self_loops, degree

class TAGCN(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, num_layers):
        super(TAGCN, self).__init__()
        self.convs = nn.ModuleList()
        self.convs.append(TAGConv(input_dim, hidden_dim))
        for _ in range(num_layers - 1):
            self.convs.append(TAGConv(hidden_dim, hidden_dim))
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        for conv in self.convs:
            x = conv(x, edge_index)
            x = F.relu(x)
        x = self.fc(x)
        return x
