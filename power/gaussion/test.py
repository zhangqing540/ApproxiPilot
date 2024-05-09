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

input_dim = 4
hidden_dim = 300
output_dim = 1
initial_learning_rate = 0.0005
num_epochs = 300
batch_size=1
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model=GraphSAGE(input_dim, hidden_dim, output_dim,batch_size=batch_size).to(device)
model.load_state_dict(torch.load("checkpoint/gsae_sobel_power_4w.pth"))

optimizer = optim.Adam(model.parameters(), lr=initial_learning_rate)
scheduler= lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', patience=10, factor=0.1, verbose=True)

test_dataset=test_dataset(root="data/test")
test_loader=DataLoader(test_dataset,batch_size=1,shuffle=False)

criterion=nn.MSELoss()

best_loss = float('inf')
best_model = None

model.eval()
with torch.no_grad():
    with open("result/pred.txt","w") as pred_file,open("result/label.txt","w") as label_file:
        for data in test_loader:
            data=data.to(device)
            optimizer.zero_grad()
            output = model(data)
            output_float=[round(float(element),2) for element in output[0]]
            output_line=" ".join(map(str,output_float))
            data_float=[round(float(element),2) for element in data.y]
            data_line=" ".join(map(str,data_float))
            pred_file.write(output_line+"\n")
            label_file.write(data_line + "\n")
