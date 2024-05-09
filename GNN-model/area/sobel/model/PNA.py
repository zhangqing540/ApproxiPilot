import torch
from torch.nn import Linear
import torch.nn.functional as F
from torch_geometric.nn import PNAConv
import torch.nn as nn

class PNAModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, num_layers):
        super(PNAModel, self).__init__()
        self.num_layers = num_layers
        self.convs = nn.ModuleList()
        for i in range(num_layers):
            self.convs.append(PNAConv(in_channels=input_dim if i == 0 else hidden_dim,
                                      out_channels=hidden_dim,
                                      aggregators=['mean', 'min', 'max'],
                                      scalers=['identity', 'amplification'],
                                      deg='learnable',
                                      edge_dim=None,
                                      towers=2))
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        for i in range(self.num_layers):
            x = F.relu(self.convs[i](x, edge_index))
        x = self.fc(x)
        return x
