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

input_dim = 12
hidden_dim = 32
output_dim = 1
initial_learning_rate = 0.0005
num_epochs = 300
batch_size=1
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model=GraphSAGE(input_dim, hidden_dim, output_dim,batch_size=batch_size).to(device)
model.load_state_dict(torch.load("checkpoint/import/latency_gsae_best.pth"))

optimizer = optim.Adam(model.parameters(), lr=initial_learning_rate)
scheduler= lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', patience=10, factor=0.1, verbose=True)

test_dataset=test_dataset(root="data/test")
test_loader=DataLoader(test_dataset,batch_size=1,shuffle=True)

criterion=nn.MSELoss()

best_loss = float('inf')
best_model = None

model.eval()
with torch.no_grad():
    area_output=[]
    area_target=[]
    latency_output = []
    latency_target = []
    power_output = []
    power_target = []
    ssim_output = []
    ssim_target = []
    all_target=[]
    all_output=[]
    for data in test_loader:
        data=data.to(device)
        optimizer.zero_grad()
        output = model(data.x,edge_index=torch.tensor([[0,1,2,3],[2,3,4,4]],dtype=torch.long,device=device))

        #print(output, data.y)
        area_output.append(output.item())
        area_target.append(data.y.item())
        print("....")
area_output=np.array(area_output)
area_target=np.array(area_target)
np.savetxt("./result/sobel_4k/latency_output.txt",area_output)
np.savetxt("./result/sobel_4k/latency_target.txt",area_target)

'''
model.eval()
with torch.no_grad():
    area_output=[]
    area_target=[]
    latency_output = []
    latency_target = []
    power_output = []
    power_target = []
    ssim_output = []
    ssim_target = []
    for data in test_loader:
        output=model(data.x,edge_index=torch.tensor([[0,1,2,3],[2,3,4,4]],dtype=torch.long))
        area_output.append(output[0].item())
        area_target.append(data.y[0].item())
        latency_output.append(output[0].item())
        latency_target.append(data.y[0].item())
        power_output.append(output[0].item())
        power_target.append(data.y[0].item())
        ssim_output.append(output[0].item())
        ssim_target.append(data.y[0].item())
        print("....")
area_output=np.array(area_output)
area_target=np.array(area_target)
area_mse=mean_squared_error(area_target,area_output)
power_output=np.array(area_output)
power_target=np.array(area_target)
power_mse=mean_squared_error(power_target,power_output)
latency_output=np.array(area_output)
latency_target=np.array(area_target)
latency_mse=mean_squared_error(latency_target,latency_output)
ssim_output=np.array(ssim_output)
ssim_target=np.array(ssim_target)
ssim_mse=mean_squared_error(ssim_target,ssim_output)
np.savetxt("./result/area_output.txt",area_output)
np.savetxt("./result/area_target.txt",area_target)
np.savetxt("./result/power_output.txt",power_output)
np.savetxt("./result/power_target.txt",power_target)
np.savetxt("./result/latency_output.txt",latency_output)
np.savetxt("./result/latency_target.txt",latency_target)
np.savetxt("./result/ssim_output.txt",ssim_output)
np.savetxt("./result/ssim_target.txt",ssim_target)
with open("./result/final.txt","w") as f_end:
  sents="area"+area_mse+"   "+"power"+power_mse+"   "+"latency"+latency_mse+"   "+"ssim"+ssim_mse
print("area_mse",area_mse)
print("power_mse",power_mse)
print("latency_mse",latency_mse)
print("ssim_mse",ssim_mse)
'''