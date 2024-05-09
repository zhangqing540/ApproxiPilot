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
input_dim = 21
hidden_dim = 300
output_dim = 1
initial_learning_rate = 1e-4
num_epochs = 100
batch_size=1
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model=GraphSAGE(input_dim, hidden_dim, output_dim,batch_size=batch_size).to(device)
model.load_state_dict(torch.load("checkpoint/kmeans_node_classfication.pth"))
optimizer = optim.Adam(model.parameters(), lr=initial_learning_rate)
scheduler= lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', patience=10, factor=0.1, verbose=True)
train_dataset=train_dataset(root="data/train")
train_loader=DataLoader(train_dataset,batch_size=batch_size,shuffle=True)
criterion=nn.CrossEntropyLoss()
best_loss = float('inf')
best_model = None

for epoch in range(num_epochs):
    model.train()
    epoch_loss = 0
    test_loss = 0
    correct = 0
    total = 0
    for data in train_loader:
        data=data.to(device)
        optimizer.zero_grad()
        output = model(data)
        new_data = data.y.reshape(batch_size, 19)
        loss = criterion(output,new_data)
        loss.backward()
        optimizer.step()
        out_,out_predicted=torch.topk(output[0],k=6)
        pred_,pred_label=torch.topk(new_data[0],k=6)
        sort_out,index_out=torch.sort(out_predicted)
        sort_label,index_label=torch.sort(pred_label)
        print("idx_out",sort_out)
        print("idx_label",sort_label)
        exit()
        correct += sort_out.eq(sort_label).sum().item()
    print(correct)
    acc = correct /420000
    scheduler.step(acc)
    print('Epoch: {:03d}, Loss: {:.4f}'.format(epoch,acc))
    torch.save(model.state_dict(), "checkpoint/kmeans_node_classfication.pth")


