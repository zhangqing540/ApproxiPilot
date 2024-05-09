import torch
from torch.nn import Linear
import torch.nn.functional as F
from torch_geometric.nn import GCNConv,GATConv,MessagePassing
import torch.nn as nn
from torch_geometric.utils import  add_self_loops,degree
from torch_geometric.nn import SAGEConv
#area
#sobel
class GraphSAGE_area_sobel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, batch_size, num_neighbors=4):
        super(GraphSAGE_area_sobel, self).__init__()
        self.batch_size=batch_size
        self.conv1 = SAGEConv(input_dim, hidden_dim)
        self.conv2 = SAGEConv(hidden_dim, hidden_dim)
        self.conv3 = SAGEConv(hidden_dim, hidden_dim)
        self.conv4 = SAGEConv(hidden_dim, hidden_dim)
        self.conv5 = SAGEConv(hidden_dim, hidden_dim)
        self.fc = nn.Linear(hidden_dim*5, output_dim)

    def forward(self,x,edge_index ):
        x = F.relu(self.conv1(x, edge_index))
        x = F.relu(self.conv2(x, edge_index))
        x = F.relu(self.conv3(x, edge_index))
        x = F.relu(self.conv4(x, edge_index))
        x = F.relu(self.conv5(x, edge_index))
        x = x.view(self.batch_size, -1, x.shape[-1])
        x=x.view(self.batch_size,-1)
        x = self.fc(x)
        return x
#gaussion
class GraphSAGE_gaussion_area(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, batch_size, num_neighbors=4):
        super(GraphSAGE_gaussion_area, self).__init__()
        self.batch_size=batch_size
        self.conv1 = SAGEConv(input_dim, hidden_dim)
        self.conv2 = SAGEConv(hidden_dim, hidden_dim)
        self.conv3 = SAGEConv(hidden_dim, hidden_dim)
        self.conv4 = SAGEConv(hidden_dim, hidden_dim)
        self.conv5 = SAGEConv(hidden_dim, hidden_dim)
        self.fc = nn.Linear(hidden_dim*17, output_dim)

    def forward(self, x,edge_index):
        x = F.relu(self.conv1(x, edge_index))
        x = F.relu(self.conv2(x, edge_index))
        x = F.relu(self.conv3(x, edge_index))
        x = F.relu(self.conv4(x, edge_index))
        x = F.relu(self.conv5(x, edge_index))
        x = x.view(self.batch_size, -1, x.shape[-1])
        x=x.view(self.batch_size,-1)
        x = self.fc(x)
        return x
#power sobel
class GraphSAGE_power_sobel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, batch_size, num_neighbors=4):
        super(GraphSAGE_power_sobel, self).__init__()
        self.batch_size=batch_size
        self.conv1 = SAGEConv(input_dim, hidden_dim)
        self.conv2 = SAGEConv(hidden_dim, hidden_dim)
        self.conv3 = SAGEConv(hidden_dim, hidden_dim)
        self.conv4 = SAGEConv(hidden_dim, hidden_dim)
        self.conv5 = SAGEConv(hidden_dim, hidden_dim)
        self.fc = nn.Linear(hidden_dim*5, output_dim)

    def forward(self, x,edge_index):
        x = F.relu(self.conv1(x, edge_index))
        x = F.relu(self.conv2(x, edge_index))
        x = F.relu(self.conv3(x, edge_index))
        x = F.relu(self.conv4(x, edge_index))
        x = F.relu(self.conv5(x, edge_index))
        x = x.view(self.batch_size, -1, x.shape[-1])
        x=x.view(self.batch_size,-1)
        x = self.fc(x)
        return x
#power gaussion
class GraphSAGE_gaussion_power(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, batch_size, num_neighbors=4):
        super(GraphSAGE_gaussion_power, self).__init__()
        self.batch_size=batch_size
        self.conv1 = SAGEConv(input_dim, hidden_dim)
        self.conv2 = SAGEConv(hidden_dim, hidden_dim)
        self.conv3 = SAGEConv(hidden_dim, hidden_dim)
        self.conv4 = SAGEConv(hidden_dim, hidden_dim)
        self.conv5 = SAGEConv(hidden_dim, hidden_dim)
        self.fc = nn.Linear(hidden_dim*17, output_dim)

    def forward(self,  x,edge_index):
        x = F.relu(self.conv1(x, edge_index))
        x = F.relu(self.conv2(x, edge_index))
        x = F.relu(self.conv3(x, edge_index))
        x = F.relu(self.conv4(x, edge_index))
        x = F.relu(self.conv5(x, edge_index))
        x = x.view(self.batch_size, -1, x.shape[-1])
        x=x.view(self.batch_size,-1)
        x = self.fc(x)
        return x
#ssim sobel
class GraphSAGE_ssim_sobel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, batch_size, num_neighbors=4):
        super(GraphSAGE_ssim_sobel, self).__init__()
        self.batch_size=batch_size
        self.conv1 = SAGEConv(input_dim, hidden_dim)
        self.conv2 = SAGEConv(hidden_dim, hidden_dim)
        self.conv3 = SAGEConv(hidden_dim, hidden_dim)
        self.conv4 = SAGEConv(hidden_dim, hidden_dim)
        self.conv5 = SAGEConv(hidden_dim, hidden_dim)
        self.fc = nn.Linear(hidden_dim*5, output_dim)

    def forward(self, x,edge_index):
        x = F.relu(self.conv1(x, edge_index))
        x = F.relu(self.conv2(x, edge_index))
        x = F.relu(self.conv3(x, edge_index))
        x = F.relu(self.conv4(x, edge_index))
        x = F.relu(self.conv5(x, edge_index))
        x = x.view(self.batch_size, -1, x.shape[-1])
        x=x.view(self.batch_size,-1)
        x = self.fc(x)
        x = torch.sigmoid(x)
        return x
#ssim gaussion
class GraphSAGE_gaussion_ssim(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, batch_size, num_neighbors=4):
        super(GraphSAGE_gaussion_ssim, self).__init__()
        self.batch_size=batch_size
        self.conv1 = SAGEConv(input_dim, hidden_dim)
        self.conv2 = SAGEConv(hidden_dim, hidden_dim)
        self.conv3 = SAGEConv(hidden_dim, hidden_dim)
        self.conv4 = SAGEConv(hidden_dim, hidden_dim)
        self.conv5 = SAGEConv(hidden_dim, hidden_dim)
        self.fc = nn.Linear(hidden_dim*17, output_dim)

    def forward(self,  x,edge_index):
        x = F.relu(self.conv1(x, edge_index))
        x = F.relu(self.conv2(x, edge_index))
        x = F.relu(self.conv3(x, edge_index))
        x = F.relu(self.conv4(x, edge_index))
        x = F.relu(self.conv5(x, edge_index))
        x = x.view(self.batch_size, -1, x.shape[-1])
        x=x.view(self.batch_size,-1)
        x = self.fc(x)
        x = torch.sigmoid(x)
        return x
#latency_node sobel
class GraphSAGE_node_calssfication_sobel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, batch_size=1, num_neighbors=4):
        super(GraphSAGE_node_calssfication_sobel, self).__init__()
        self.batch_size = batch_size
        self.input_dim = input_dim
        self.conv1 = SAGEConv(input_dim, hidden_dim)
        self.conv2 = SAGEConv(hidden_dim, output_dim)
        self.conv3 = SAGEConv(hidden_dim, output_dim)
        self.conv4 = SAGEConv(hidden_dim, hidden_dim)
        self.conv5 = SAGEConv(hidden_dim, output_dim)
        self.fc1 = nn.Linear(5100, 1024)
        self.fc2 = nn.Linear(1024, 128)
        self.fc3 = nn.Linear(128, output_dim)
    def forward(self, x,edge_index):
        x = F.relu(self.conv1(x, edge_index))
        x = F.relu(self.conv2(x, edge_index))
        x = x.view(self.batch_size, 5)
        return x
#latency_node gaussion
class GraphSAGE_node_classfication_gaussion(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, batch_size, num_neighbors=4):
        super(GraphSAGE_node_classfication_gaussion, self).__init__()
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

    def forward(self, x,edge_index):
        x = F.relu(self.conv1(x, edge_index))
        x = F.relu(self.conv2(x, edge_index))
        x = F.relu(self.conv3(x, edge_index))
        x = F.relu(self.conv4(x, edge_index))
        x = F.relu(self.conv5(x, edge_index))
        x = x.view(self.batch_size,17)
        return x
#latency sobel
class GraphSAGE_latency_sobel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, batch_size, num_neighbors=4):
        super(GraphSAGE_latency_sobel, self).__init__()
        self.batch_size=batch_size
        self.conv1 = SAGEConv(input_dim, hidden_dim)
        self.conv2 = SAGEConv(hidden_dim, hidden_dim)
        self.conv3 = SAGEConv(hidden_dim, hidden_dim)
        self.conv4 = SAGEConv(hidden_dim, hidden_dim)
        self.conv5 = SAGEConv(hidden_dim, hidden_dim)
        self.fc1= nn.Linear(hidden_dim*5, output_dim)
    def forward(self, x,edge_index):
        x = F.relu(self.conv1(x, edge_index))
        x = F.relu(self.conv2(x, edge_index))
        x = F.relu(self.conv3(x, edge_index))
        x = F.relu(self.conv4(x, edge_index))
        x = F.relu(self.conv5(x, edge_index))
        x = x.view(self.batch_size, -1, x.shape[-1])
        x=x.view(self.batch_size,-1)
        x = self.fc1(x)
        return x
#latency gaussion
class GraphSAGE_latency_gaussion(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, batch_size, num_neighbors=4):
        super(GraphSAGE_latency_gaussion, self).__init__()
        self.batch_size=batch_size
        self.conv1 = SAGEConv(input_dim, hidden_dim)
        self.conv2 = SAGEConv(hidden_dim, hidden_dim)
        self.conv3 = SAGEConv(hidden_dim, hidden_dim)
        self.conv4 = SAGEConv(hidden_dim, hidden_dim)
        self.conv5 = SAGEConv(hidden_dim, hidden_dim)
        self.fc1= nn.Linear(hidden_dim*17, output_dim)
    def forward(self,  x,edge_index):
        x = F.relu(self.conv1(x, edge_index))
        x = F.relu(self.conv2(x, edge_index))
        x = F.relu(self.conv3(x, edge_index))
        x = F.relu(self.conv4(x, edge_index))
        x = F.relu(self.conv5(x, edge_index))
        x = x.view(self.batch_size, -1, x.shape[-1])
        x=x.view(self.batch_size,-1)
        x = self.fc1(x)
        return x
#node classfication
class node_classfication_kmeans_GraphSAGE(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, batch_size, num_neighbors=4):
        super(node_classfication_kmeans_GraphSAGE, self).__init__()
        self.batch_size = batch_size
        self.input_dim=input_dim
        self.conv1 = SAGEConv(input_dim, hidden_dim)
        self.conv2 = SAGEConv(hidden_dim, hidden_dim)
        self.conv3 = SAGEConv(hidden_dim, hidden_dim)
        self.conv4 = SAGEConv(hidden_dim, hidden_dim)
        self.conv5 = SAGEConv(hidden_dim, hidden_dim)
        self.conv6 = SAGEConv(hidden_dim, hidden_dim)
        self.conv7 = SAGEConv(hidden_dim, output_dim)
        self.fc1=nn.Linear(5100,1024)
        self.fc2=nn.Linear(1024,128)
        self.fc3 = nn.Linear(128, output_dim)

    def forward(self,x,edge_index):
        x = F.relu(self.conv1(x, edge_index))
        x = F.relu(self.conv2(x, edge_index))
        x = F.relu(self.conv3(x, edge_index))
        x = F.relu(self.conv4(x, edge_index))
        x = F.relu(self.conv5(x, edge_index))
        x = F.relu(self.conv6(x, edge_index))
        x = F.relu(self.conv7(x, edge_index))

        x = x.view(self.batch_size,19)

        return x
#latency kmeans
class top_latency_kmeans_GraphSAGE(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, batch_size, num_neighbors=4):
        super(top_latency_kmeans_GraphSAGE, self).__init__()
        self.batch_size=batch_size
        self.conv1 = SAGEConv(input_dim, hidden_dim)
        self.conv2 = SAGEConv(hidden_dim, hidden_dim)
        self.conv3 = SAGEConv(hidden_dim, hidden_dim)
        self.conv4 = SAGEConv(hidden_dim, hidden_dim)
        self.conv5 = SAGEConv(hidden_dim, hidden_dim)
        self.fc1= nn.Linear(hidden_dim*19, output_dim)
    def forward(self, x_mian,edge_index_mian):
        x_mian = F.relu(self.conv1(x_mian, edge_index_mian))
        x_mian = F.relu(self.conv2(x_mian, edge_index_mian))
        x_mian = F.relu(self.conv3(x_mian, edge_index_mian))
        x_mian = F.relu(self.conv4(x_mian, edge_index_mian))
        x_mian = F.relu(self.conv5(x_mian, edge_index_mian))
        x_mian = x_mian.view(self.batch_size, -1, x_mian.shape[-1])
        x_mian=x_mian.view(self.batch_size,-1)
        x_mian = self.fc1(x_mian)
        return x_mian
#ssim kmeans
class ssim_kmeans_GraphSAGE(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, batch_size, num_neighbors=4):
        super(ssim_kmeans_GraphSAGE, self).__init__()
        self.batch_size=batch_size
        self.conv1 = SAGEConv(input_dim, hidden_dim)
        self.conv2 = SAGEConv(hidden_dim, hidden_dim)
        self.conv3 = SAGEConv(hidden_dim, hidden_dim)
        self.conv4 = SAGEConv(hidden_dim, hidden_dim)
        self.conv5 = SAGEConv(hidden_dim, hidden_dim)
        self.conv6 = SAGEConv(hidden_dim, hidden_dim)
        self.conv7 = SAGEConv(hidden_dim, hidden_dim)
        self.fc1 = nn.Linear(hidden_dim*17, output_dim)
        #self.fc2=nn.Linear(100, output_dim)
    def forward(self, x_mian,edge_index_mian):

        x_mian = F.relu(self.conv1(x_mian, edge_index_mian))
        x_mian = F.relu(self.conv2(x_mian, edge_index_mian))
        x_mian = F.relu(self.conv3(x_mian, edge_index_mian))
        x_mian = F.relu(self.conv4(x_mian, edge_index_mian))
        x_mian = F.relu(self.conv5(x_mian, edge_index_mian))
        x_mian = F.relu(self.conv6(x_mian, edge_index_mian))
        x_mian = F.relu(self.conv7(x_mian, edge_index_mian))
        x_mian = x_mian.view(self.batch_size, -1, x_mian.shape[-1])
        x_mian=x_mian.view(self.batch_size,-1)
        x_mian = self.fc1(x_mian)
        #x_mian = self.fc2(x_mian)
        x_mian = torch.sigmoid(x_mian)
        return x_mian
#area kmeans
class area_kmeans_GraphSAGE(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, batch_size, num_neighbors=4):
        super(area_kmeans_GraphSAGE, self).__init__()
        self.batch_size=batch_size
        self.conv1 = SAGEConv(input_dim, hidden_dim)
        self.conv2 = SAGEConv(hidden_dim, hidden_dim)
        self.conv3 = SAGEConv(hidden_dim, hidden_dim)
        self.conv4 = SAGEConv(hidden_dim, hidden_dim)
        self.conv5 = SAGEConv(hidden_dim, hidden_dim)
        self.fc = nn.Linear(hidden_dim*24, output_dim)

    def forward(self, x_mian,edge_index_mian):
        x_mian = F.relu(self.conv1(x_mian, edge_index_mian))
        x_mian = F.relu(self.conv2(x_mian, edge_index_mian))
        x_mian = F.relu(self.conv3(x_mian, edge_index_mian))
        x_mian = F.relu(self.conv4(x_mian, edge_index_mian))
        x_mian = F.relu(self.conv5(x_mian, edge_index_mian))
        x_mian = x_mian.view(self.batch_size, -1, x_mian.shape[-1])
        x_mian=x_mian.view(self.batch_size,-1)
        x_mian = self.fc(x_mian)
        return x_mian
#power kmeans
class power_kmeans_GraphSAGE(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, batch_size, num_neighbors=4):
        super(power_kmeans_GraphSAGE, self).__init__()
        self.batch_size=batch_size
        self.conv1 = SAGEConv(input_dim, hidden_dim)
        self.conv2 = SAGEConv(hidden_dim, hidden_dim)
        self.conv3 = SAGEConv(hidden_dim, hidden_dim)
        self.conv4 = SAGEConv(hidden_dim, hidden_dim)
        self.conv5 = SAGEConv(hidden_dim, hidden_dim)
        self.fc = nn.Linear(hidden_dim*24, output_dim)

    def forward(self,x_mian,edge_index_mian):
        x_mian = F.relu(self.conv1(x_mian, edge_index_mian))
        x_mian = F.relu(self.conv2(x_mian, edge_index_mian))
        x_mian = F.relu(self.conv3(x_mian, edge_index_mian))
        x_mian = F.relu(self.conv4(x_mian, edge_index_mian))
        x_mian = F.relu(self.conv5(x_mian, edge_index_mian))
        x_mian = x_mian.view(self.batch_size, -1, x_mian.shape[-1])
        x_mian=x_mian.view(self.batch_size,-1)
        x_mian = self.fc(x_mian)
        return x_mian