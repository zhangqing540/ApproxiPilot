import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch_geometric.data import InMemoryDataset, Data
from torch_geometric.nn import GCNConv
from torch_geometric.loader import DataLoader
from gnn_model.model import GraphSAGE_gaussion_area,GraphSAGE_latency_gaussion,GraphSAGE_gaussion_ssim,GraphSAGE_gaussion_power,GraphSAGE_node_classfication_gaussion
import torch.optim.lr_scheduler as lr_scheduler
import numpy as np
from sklearn.metrics import mean_squared_error
from gnn_model.ultils import *
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
edge_index = torch.tensor([[0, 9, 1, 9, 2, 10, 3, 10, 4, 11, 5, 11, 6, 12, 7, 12, 8, 16, 9, 13, 10, 13, 11, 14,12, 14, 13, 15, 14, 15, 15, 16],[9, 0, 9, 1, 10, 2, 10, 3, 11, 4, 11, 5, 12, 6, 12, 7, 16, 8, 13, 9, 13, 10, 14, 11,14, 12, 15, 13, 15, 14, 16, 15]], dtype=torch.long, device=device)
model_area = GraphSAGE_gaussion_area(4, 300, 1, batch_size=1).to(device)
model_area.load_state_dict(torch.load("F:\software_code\近似计算\sample_test_gaussion\gnn_model\checkpoint\gaussion/gsae_area_gaussion.pth", map_location=device))
model_power = GraphSAGE_gaussion_power(4, 300, 1, batch_size=1).to(device)
model_power.load_state_dict(torch.load("F:\software_code\近似计算\sample_test_gaussion\gnn_model\checkpoint/gaussion/gsae_gaussion_power.pth", map_location=device))
model_node_classfication = GraphSAGE_node_classfication_gaussion(input_dim=21,hidden_dim=300,output_dim=1, batch_size=1).to(device)
model_node_classfication.load_state_dict(torch.load("F:\software_code\近似计算\sample_test_gaussion\gnn_model\checkpoint\gaussion/gase_gaussion_node_classfication.pth",map_location=device))
model_latency = GraphSAGE_latency_gaussion(17, 300, 1, batch_size=1).to(device)
model_latency.load_state_dict(torch.load("F:\software_code\近似计算\sample_test_gaussion\gnn_model\checkpoint\gaussion/gsae_gaussion_latency.pth",map_location=device))
model_ssim = GraphSAGE_gaussion_ssim(12, 300, 1, batch_size=1).to(device)
model_ssim.load_state_dict(torch.load("F:\software_code\近似计算\sample_test_gaussion\gnn_model\checkpoint\gaussion/gsae_gaussion_ssim.pth", map_location=device))
def sample_test(single_design):
    with torch.no_grad():
        area_data_in= single_design_totensor_area_gaussion(single_design).to(device)
        area_output = model_area(area_data_in,edge_index=edge_index)
        power_data_in = single_design_totensor_power_gaussion(single_design).to(device)
        power_output = model_power(power_data_in,edge_index=edge_index)
        ssim_data_in = single_design_totensor_gaussion_ssim(single_design).to(device)
        ssim_output = model_ssim(ssim_data_in, edge_index=edge_index)
        single_design_link_in = single_design_totensor_gaussion_node(single_design).to(device)
        node_link_output=model_node_classfication(single_design_link_in,edge_index=edge_index)
        node_link_output_, node_link_output_index = torch.topk(node_link_output, k=5)
        new_node_link_index=node_link_output_index.tolist()
        single_design_link=[single_design[idx] for idx in new_node_link_index[0]]
        latency_data_in = single_design_totensor_gaussion_link(single_design, single_design_link).to(device)
        latency_output = model_latency(latency_data_in, edge_index=edge_index)
    area=area_output.item()*2000
    power = power_output.item() * 2000
    latency=latency_output.item()*3
    ssim=ssim_output.item()
    return area,power,latency,ssim
