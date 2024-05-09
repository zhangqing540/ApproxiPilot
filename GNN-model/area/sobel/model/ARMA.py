import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import ARMAConv


class GraphARMA(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, batch_size, num_layers=5):
        super(GraphARMA, self).__init__()
        self.batch_size = batch_size
        self.num_layers = num_layers

        # ARMAConv layers
        self.conv_layers = nn.ModuleList()
        self.conv_layers.append(ARMAConv(input_dim, hidden_dim))
        for _ in range(num_layers - 1):
            self.conv_layers.append(ARMAConv(hidden_dim, hidden_dim))

        # Fully connected layer
        self.fc = nn.Linear(hidden_dim * num_layers, output_dim)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index

        # Apply ARMAConv layers
        for conv in self.conv_layers:
            x = F.relu(conv(x, edge_index))

        # Reshape and apply fully connected layer
        x = x.view(self.batch_size, -1, x.shape[-1])
        x = x.view(self.batch_size, -1)
        x = self.fc(x)

        return x
