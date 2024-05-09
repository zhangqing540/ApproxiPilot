import torch
from torch.nn import Linear
import torch.nn.functional as F
from torch_geometric.nn import PANConv
import torch.nn as nn
from torch_geometric.utils import add_self_loops, degree

class PANNet(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, num_layers):
        super(PANNet, self).__init__()
        self.num_layers = num_layers
        self.convs = nn.ModuleList()
        self.convs.append(PANConv(input_dim, hidden_dim))

        for _ in range(self.num_layers - 1):
            self.convs.append(PANConv(hidden_dim, hidden_dim))

        self.lin = Linear(hidden_dim, output_dim)

    def forward(self, data):
        x, edge_index, batch = data.x, data.edge_index, data.batch

        for i in range(self.num_layers):
            x = F.relu(self.convs[i](x, edge_index))

        x = self.lin(x)
        return F.log_softmax(x, dim=1)
