import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch_geometric.data import InMemoryDataset, Data
from torch_geometric.nn import GCNConv
from torch_geometric.loader import DataLoader
from gnn_model.model import *
import torch.optim.lr_scheduler as lr_scheduler
import numpy as np
from sklearn.metrics import mean_squared_error
from gnn_model.ultils import *
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
edge_index_all = graph_link("F:\software_code\近似计算\sample_test\gnn_model/edge_index/link.txt")
edge_index_part=graph_link("F:\software_code\近似计算\sample_test\gnn_model/edge_index/part_link.txt")
edge_index_ssim=graph_link("F:\software_code\近似计算\sample_test\gnn_model/edge_index/kmeans_link.txt")
model_area = area_kmeans_GraphSAGE(4, 300, 1, batch_size=1).to(device)
model_area.load_state_dict(torch.load("F:\software_code\近似计算\sample_test\gnn_model\checkpoint\kmeans/gsae_area_kmeans_7w.pth", map_location=device))
model_power = power_kmeans_GraphSAGE(4, 300, 1, batch_size=1).to(device)
model_power.load_state_dict(torch.load("F:\software_code\近似计算\sample_test\gnn_model\checkpoint/kmeans/gsae_power_kmeans_7w.pth", map_location=device))
model_node_classfication = node_classfication_kmeans_GraphSAGE(input_dim=21,hidden_dim=300,output_dim=1, batch_size=1).to(device)
model_node_classfication.load_state_dict(torch.load("F:\software_code\近似计算\sample_test\gnn_model\checkpoint\kmeans/kmeans_node_classfication.pth",map_location=device))
model_latency = top_latency_kmeans_GraphSAGE(17, 300, 1, batch_size=1).to(device)
model_latency.load_state_dict(torch.load("F:\software_code\近似计算\sample_test\gnn_model\checkpoint\kmeans/gsae_kmeans_latency_import.pth",map_location=device))
model_ssim = ssim_kmeans_GraphSAGE(13, 300, 1, batch_size=1).to(device)
model_ssim.load_state_dict(torch.load("F:\software_code\近似计算\sample_test\gnn_model\checkpoint\kmeans/gsae_kmeans_ssim_10w.pth", map_location=device))
def sample_test(single_design):
    with torch.no_grad():
        area_data_in= single_design_totensor_kmeans_area(single_design).to(device)
        area_output = model_area(area_data_in,edge_index_all)
        power_data_in = single_design_totensor_kmeans_power(single_design).to(device)
        power_output = model_power(power_data_in,edge_index_all)
        ssim_data_in = single_design_totensor_kmeans_ssim(single_design).to(device)
        ssim_output = model_ssim(ssim_data_in,edge_index_ssim)
        single_design_link_in = single_design_totensor_kmeans_node(single_design).to(device)
        node_link_output=model_node_classfication(single_design_link_in,edge_index=edge_index_part)
        node_link_output_, node_link_output_index = torch.topk(node_link_output, k=6)
        sort_out,new_node_link_index  = torch.sort(node_link_output_index, descending=True)
        latency_data_in = single_design_totensor_kmeans_latency(single_design, sort_out).to(device)
        latency_output = model_latency(latency_data_in, edge_index_part)
    area=area_output.item()*20000
    power = power_output.item() * 1000
    latency=latency_output.item()*20
    ssim=ssim_output.item()
    return area,power,latency,ssim
