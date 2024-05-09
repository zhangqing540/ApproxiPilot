import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch_geometric.data import InMemoryDataset, Data
from torch_geometric.nn import GCNConv
from torch_geometric.loader import DataLoader
from model.gat import GAT
from model.gsae import GraphSAGE
from model.gcn import GCN
from model.mpnn import MPNN
from  ultils import test_dataset
import torch.optim.lr_scheduler as lr_scheduler
import numpy as np
from sklearn.metrics import mean_squared_error
input_dim = 21
hidden_dim = 300
output_dim = 1
initial_learning_rate = 0.0005
num_epochs = 300
batch_size=1
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model=GraphSAGE(input_dim, hidden_dim, output_dim,batch_size=batch_size).to(device)
model.load_state_dict(torch.load("checkpoint/kmeans_node_classfication.pth"))
optimizer = optim.Adam(model.parameters(), lr=initial_learning_rate)
scheduler= lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', patience=10, factor=0.1, verbose=True)
test_dataset=test_dataset(root="data/test")
test_loader=DataLoader(test_dataset,batch_size=1,shuffle=False)
best_loss = float('inf')
best_model = None
model.eval()
test_loss=0
correct=0
total=0
with torch.no_grad():
    for data in test_loader:
        data=data.to(device)
        optimizer.zero_grad()
        output = model(data)
        out_, out_predicted = torch.topk(output, k=6)
        pred_, pred_label = torch.topk(data.y, k=6)
        sort_out, index_out = torch.sort(out_predicted, descending=True)
        sort_label, index_label = torch.sort(pred_label, descending=True)
        correct += sort_out.eq(sort_label).sum().item()
    print(correct)
    acc = correct / (2490*6)
    print(acc)
