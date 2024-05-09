import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch_geometric.data import InMemoryDataset, Data
from torch_geometric.nn import GCNConv
from torch_geometric.loader import DataLoader
from gnn_model.model import GraphSAGE_area_sobel,GraphSAGE_latency_sobel,GraphSAGE_ssim_sobel,GraphSAGE_power_sobel,GraphSAGE_node_calssfication_sobel
import torch.optim.lr_scheduler as lr_scheduler
import numpy as np
from sklearn.metrics import mean_squared_error
from gnn_model.ultils import *
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
edge_index = torch.tensor([[0, 2, 1, 3, 2, 4, 3, 4],[2, 0, 3, 1, 4, 2, 4, 3]], dtype=torch.long, device=device)
model_area = GraphSAGE_area_sobel(4, 300, 1, batch_size=1).to(device)
model_area.load_state_dict(torch.load("F:\software_code\近似计算\sample_test_gaussion\gnn_model\checkpoint\sobel/gsae_area_sobel_4w.pth", map_location=device))
model_power = GraphSAGE_power_sobel(4, 300, 1, batch_size=1).to(device)
model_power.load_state_dict(torch.load("F:\software_code\近似计算\sample_test_gaussion\gnn_model\checkpoint/sobel/gsae_sobel_power_4w.pth", map_location=device))
model_node_classfication = GraphSAGE_node_calssfication_sobel(input_dim=19,hidden_dim=300,output_dim=1, batch_size=1).to(device)
model_node_classfication.load_state_dict(torch.load("F:\software_code\近似计算\sample_test_gaussion\gnn_model\checkpoint\sobel/sobel_node_classfication.pth",map_location=device))
model_latency = GraphSAGE_latency_sobel(17, 300, 1, batch_size=1).to(device)
model_latency.load_state_dict(torch.load("F:\software_code\近似计算\sample_test_gaussion\gnn_model\checkpoint\sobel/gsae_sobel_latency_4w.pth",map_location=device))
model_ssim = GraphSAGE_ssim_sobel(12, 300, 1, batch_size=1).to(device)
model_ssim.load_state_dict(torch.load("F:\software_code\近似计算\sample_test_gaussion\gnn_model\checkpoint\sobel/gsae_ssim_sobel_4w.pth", map_location=device))
def sample_test(add81,add82,add91,add92,sub10):
    single_design=[add81,add82,add91,add92,sub10]
    with torch.no_grad():
        area_power_data_in= single_design_totensor_area_power(single_design).to(device)
        area_output = model_area(area_power_data_in,edge_index=edge_index)
        power_output = model_power(area_power_data_in,edge_index=edge_index)
        ssim_data_in = single_design_totensor_ssim(single_design).to(device)
        ssim_output = model_ssim(ssim_data_in, edge_index=edge_index)
        single_design_link_in = single_design_totensor_node(single_design).to(device)
        node_link_output=model_node_classfication(single_design_link_in,edge_index=edge_index)
        node_link_output_, node_link_output_index = torch.topk(node_link_output, k=3)
        new_node_link_index=node_link_output_index.tolist()
        single_design_link=[single_design[idx] for idx in new_node_link_index[0]]
        latency_data_in = single_design_totensor_latency(single_design, single_design_link).to(device)
        latency_output = model_latency(latency_data_in, edge_index=edge_index)
    area=area_output.item()*200
    power=power_output.item()*5
    latency=latency_output.item()
    ssim=ssim_output.item()
    return area,power,latency,ssim
