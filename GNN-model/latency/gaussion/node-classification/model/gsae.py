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
        self.batch_size = batch_size
        self.input_dim=input_dim
        self.conv1 = SAGEConv(input_dim, hidden_dim)
        self.conv2 = SAGEConv(hidden_dim, hidden_dim)
        self.conv3 = SAGEConv(hidden_dim, hidden_dim)
        self.conv4 = SAGEConv(hidden_dim, hidden_dim)
        self.conv5 = SAGEConv(hidden_dim, output_dim)
        self.fc1=nn.Linear(5100,1024)
        self.fc2=nn.Linear(1024,128)
        self.fc3 = nn.Linear(128, output_dim)

    def forward(self,data):
        x,edge_index=data.x,data.edge_index
        #print("in",x)
        x = F.relu(self.conv1(x, edge_index))
        #print("1", x)
        x = F.relu(self.conv2(x, edge_index))
        #print("2", x)
        x = F.relu(self.conv3(x, edge_index))
        #print("3", x)
        x = F.relu(self.conv4(x, edge_index))
        #print("4", x)
        #exit()
        x = F.relu(self.conv5(x, edge_index))
        #x = F.relu(self.conv6(x, edge_index))
        #x = F.relu(self.conv7(x, edge_index))
        #x = x.view(self.batch_size, -1, x.shape[-1])
        #x = x.view(self.batch_size, -1)
        #x = self.fc1(x)
        #print("fc1",x)
        #x = self.fc2(x)
        #print("fc2", x)
        #x = self.fc3(x)
        #print("fc3", x)
        #exit()
        #print("22",x)
        x = x.view(self.batch_size,17)
        #print("2",x)
        #x=F.softmax(x, dim=1)
        #print("out", x)
        #exit()
        return x
