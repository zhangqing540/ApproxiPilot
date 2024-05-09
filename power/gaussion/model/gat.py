import torch
from torch.nn import Linear
import torch.nn.functional as F
from torch_geometric.nn import GCNConv,GATConv,MessagePassing
import torch.nn as nn
from torch_geometric.utils import  add_self_loops,degree
from torch_geometric.nn import SAGEConv
class GAT(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, num_heads=8):
        super(GAT, self).__init__()
        self.conv1 = GATConv(input_dim, hidden_dim, heads=num_heads)
        self.conv2 = GATConv(hidden_dim * num_heads, hidden_dim, heads=num_heads)
        self.conv3 = GATConv(hidden_dim * num_heads, hidden_dim, heads=num_heads)
        self.conv4 = GATConv(hidden_dim * num_heads, hidden_dim, heads=num_heads)
        self.fc = Linear(1280, output_dim)

    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        #print("1",x,x.shape)
        x = F.leaky_relu(x, negative_slope=0.2)  # 使用LeakyReLU作为激活函数
        x = self.conv2(x, edge_index)
        x = F.leaky_relu(x, negative_slope=0.2)  # 使用LeakyReLU作为激活函数
        x = self.conv3(x, edge_index)
        x = F.leaky_relu(x, negative_slope=0.2)  # 使用LeakyReLU作为激活函数
        x = self.conv4(x, edge_index)
        x = F.leaky_relu(x, negative_slope=0.2)  # 使用LeakyReLU作为激活函数
        x = torch.cat([x[i] for i in range(5)], dim=-1)
        x = self.fc(x)
        return x