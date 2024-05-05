import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch_geometric.data import InMemoryDataset, Data
from torch_geometric.nn import GCNConv
from torch_geometric.loader import DataLoader
from model.gat import GAT
from model.gcn import GCN
from model.mpnn import MPNN
from model.gsae import GraphSAGE
from  ultils import train_dataset
import torch.optim.lr_scheduler as lr_scheduler
input_dim = 8
hidden_dim = 32
output_dim = 1
initial_learning_rate = 1e-3
num_epochs = 50
batch_size=1
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model=GAT(input_dim, hidden_dim, output_dim).to(device)
#model.load_state_dict(torch.load("checkpoint/ori/area_gsae_best.pth"))
optimizer = optim.Adam(model.parameters(), lr=initial_learning_rate)
scheduler= lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', patience=10, factor=0.1, verbose=True)

train_dataset=train_dataset(root="data/train")
train_loader=DataLoader(train_dataset,batch_size=batch_size,shuffle=True)

criterion=nn.MSELoss()

best_loss = float('inf')
best_model = None

for epoch in range(num_epochs):
    model.train()
    epoch_loss = 0
    for data in train_loader:
        data=data.to(device)
        optimizer.zero_grad()
        #print(data.x.shape)
        output = model(data.x,edge_index=torch.tensor([[0,1,2,3],[2,3,4,4]],dtype=torch.long,device=device))
        loss = criterion(output, data.y)
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item()
    scheduler.step(epoch_loss)
    if epoch_loss < best_loss:
        best_loss = epoch_loss
        best_model = model.state_dict().copy()
        torch.save(model.state_dict(), "checkpoint/import/latency_gsae_best.pth")
    with open("./result/loss.txt", "w") as f:
        f.write(format(epoch_loss) + "\n")
    print('Epoch: {:03d}, Loss: {:.4f}'.format(epoch, epoch_loss))
    torch.save(model.state_dict(), "checkpoint/ori/gsae.pth")

