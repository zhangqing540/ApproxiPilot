import torch
from torch.nn import Linear
import torch.nn.functional as F
from torch_geometric.nn import GCNConv,GATConv,MessagePassing
import torch.nn as nn
from torch_geometric.utils import  add_self_loops,degree
from torch_geometric.nn import SAGEConv
class MPNN(MessagePassing):
    def __init__(self, input_dim, hidden_dim, output_dim,batch_size):
        super(MPNN, self).__init__(aggr='add')  # 使用'add'聚合策略
        self.batch_size = batch_size
        self.mlp = nn.Sequential(
            Linear(input_dim, hidden_dim),
            nn.ReLU(),
            Linear(hidden_dim, hidden_dim)
        )
        self.fc = Linear(5100, output_dim)

    def forward(self, data):
        # 添加自环，确保节点有自己的特征参与更新
        x, edge_index = data.x, data.edge_index
        edge_index, _ = add_self_loops(edge_index, num_nodes=x.size(0))
        # 计算归一化系数
        row, col = edge_index
        deg = degree(col, x.size(0), dtype=x.dtype)
        deg_inv_sqrt = deg.pow(-0.5)
        norm = deg_inv_sqrt[row] * deg_inv_sqrt[col]

        x = self.mlp(x)
        # 使用消息传递函数发送和聚合消息
        x = self.propagate(edge_index, x=x, norm=norm)
        x = F.relu(x)
        x = x.view(self.batch_size, -1, x.shape[-1])
        x = x.view(self.batch_size, -1)
        x = self.fc(x)
        return x

    def message(self, x_j, norm):
        # 消息传递函数，这里使用节点特征x_j乘以归一化系数norm作为消息
        return norm.view(-1, 1) * x_j