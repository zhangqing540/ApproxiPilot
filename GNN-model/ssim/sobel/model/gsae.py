import torch
from torch.nn import Linear
import torch.nn.functional as F
from torch_geometric.nn import GCNConv, GATConv, MessagePassing
import torch.nn as nn
from torch_geometric.utils import add_self_loops, degree
from torch_geometric.nn import SAGEConv,GCNConv

class GraphSAGE(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, batch_size, num_neighbors=4):
        super(GraphSAGE, self).__init__()
        self.batch_size=batch_size
        self.conv1 = SAGEConv(input_dim, hidden_dim)
        self.conv2 = SAGEConv(hidden_dim, hidden_dim)
        self.conv3 = SAGEConv(hidden_dim, hidden_dim)
        self.conv4 = SAGEConv(hidden_dim, hidden_dim)
        self.conv5 = SAGEConv(hidden_dim, hidden_dim)
        self.fc = nn.Linear(hidden_dim*5, output_dim)

    def forward(self, data):
        x_mian,edge_index_mian=data.x,data.edge_index
        x_mian = F.relu(self.conv1(x_mian, edge_index_mian))
        x_mian = F.relu(self.conv2(x_mian, edge_index_mian))
        x_mian = F.relu(self.conv3(x_mian, edge_index_mian))
        x_mian = F.relu(self.conv4(x_mian, edge_index_mian))
        x_mian = F.relu(self.conv5(x_mian, edge_index_mian))
        x_mian = x_mian.view(self.batch_size, -1, x_mian.shape[-1])
        x_mian=x_mian.view(self.batch_size,-1)
        x_mian = self.fc(x_mian)
        x_mian = torch.sigmoid(x_mian)
        return x_mian
