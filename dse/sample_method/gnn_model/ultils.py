import torch
from torch_geometric.data import InMemoryDataset,Data
import numpy as np
import torch.nn.functional as F
import ast
import math
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
def graph_link(path):
    with open(path,"r") as file:
        listA=[]
        listB=[]
        for line in file:
            single_link=line.split(" ")
            listA.append(int(single_link[0]))
            listB.append(int(single_link[1]))
    link=torch.tensor([listA,listB], dtype=torch.long, device=device)
    return link
def txt_to_dictkey(path):
    dict={}
    with open(path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            key, value = line.strip().split(': ')
            dict[key] =value
    return dict
def single_design_totensor_area_power(single_design):
    all_design_input=[]
    add8_dict=txt_to_dictkey("F:\software_code/近似计算\sample_test_gaussion\gnn_model/uint_lib/area_power/add8.txt")
    add12_dict = txt_to_dictkey("F:\software_code/近似计算\sample_test_gaussion\gnn_model/uint_lib/area_power/add12.txt")
    sub10_dict=txt_to_dictkey("F:\software_code/近似计算\sample_test_gaussion\gnn_model/uint_lib/area_power/sub10.txt")
    #print(single_design)
    for uint_design in single_design:
        if uint_design in add8_dict:
            add8_latency_in=list(eval(add8_dict.get(uint_design)))
            all_design_input.append(add8_latency_in+[1,0])
        elif uint_design in add12_dict:
            add12_latency_in = list(eval(add12_dict.get(uint_design)))
            all_design_input.append(add12_latency_in + [1, 0])
        else:
            #print(uint_design)
            sub10_latency_in = list(eval(sub10_dict.get(uint_design)))
            all_design_input.append(sub10_latency_in + [0, 1])
    return torch.tensor(all_design_input)/25
def single_design_totensor_ssim(single_design):
    all_design_input=[]
    add8_dict=txt_to_dictkey("F:\software_code/近似计算\sample_test_gaussion\gnn_model/uint_lib/ssim/pre_pruning_add8.txt")
    add12_dict = txt_to_dictkey("F:\software_code/近似计算\sample_test_gaussion\gnn_model/uint_lib/ssim/pre_pruning_add12.txt")
    sub10_dict = txt_to_dictkey("F:\software_code/近似计算\sample_test_gaussion\gnn_model/uint_lib/ssim/pre_pruning_sub10.txt")
    for idx,uint_design in enumerate(single_design):
        if uint_design in add8_dict:
            mul_ssim=list(eval(add8_dict.get(uint_design)))
            mul_ssim=[mul_ssim[0]/25,mul_ssim[1]/25,mul_ssim[2],math.log10(mul_ssim[3])+2,math.log10(mul_ssim[4])+2,math.log10(mul_ssim[5])+2,math.log10(mul_ssim[6])+2]
            all_design_input.append(mul_ssim+[1,0,1,0,0])
        elif uint_design in add12_dict:
            mul_ssim=list(eval(add12_dict.get(uint_design)))
            mul_ssim=[mul_ssim[0]/25,mul_ssim[1]/25,mul_ssim[2],math.log10(mul_ssim[3])+2,math.log10(mul_ssim[4])+2,math.log10(mul_ssim[5])+2,math.log10(mul_ssim[6])+2]
            all_design_input.append(mul_ssim+[1,0,0,1,0])
        elif uint_design in sub10_dict:
            mul_ssim=list(eval(sub10_dict.get(uint_design)))
            mul_ssim=[mul_ssim[0]/25,mul_ssim[1]/25,mul_ssim[2],math.log10(mul_ssim[3])+2,math.log10(mul_ssim[4])+2,math.log10(mul_ssim[5])+2,math.log10(mul_ssim[6])+2]
            all_design_input.append(mul_ssim+[0,1,0,0,1])
    return torch.tensor(all_design_input)
def single_design_totensor_node(single_design):
    all_design_input=[]
    add8_dict=txt_to_dictkey("F:\software_code/近似计算\sample_test_gaussion\gnn_model/uint_lib/latency/add8_dataset_latency.txt")
    add12_dict = txt_to_dictkey("F:\software_code/近似计算\sample_test_gaussion\gnn_model/uint_lib/latency/add12_dataset_latency.txt")
    sub10_dict=txt_to_dictkey("F:\software_code/近似计算\sample_test_gaussion\gnn_model/uint_lib/latency/sub10_dataset_latency.txt")
    for idx, uint_design in enumerate(single_design):
        if  idx <=1:
            add8_latency = list(eval(add8_dict.get(uint_design)))
            all_design_input.append(add8_latency + [1, 0] + [1,0,0])
        elif  2<=idx <=3:
            add12_latency = list(eval(add12_dict.get(uint_design)))
            all_design_input.append(add12_latency + [1, 0] + [0,1,0])
        elif idx==4:
            sub10_latency = list(eval(sub10_dict.get(uint_design)))
            all_design_input.append(sub10_latency + [0, 1] + [0,0,1])
    return torch.tensor(all_design_input)
def single_design_totensor_latency(single_design,single_design_link):
    all_design_input=[]
    add8_dict=txt_to_dictkey("F:\software_code/近似计算\sample_test_gaussion\gnn_model/uint_lib/latency/add8_dataset_latency.txt")
    add12_dict = txt_to_dictkey("F:\software_code/近似计算\sample_test_gaussion\gnn_model/uint_lib/latency/add12_dataset_latency.txt")
    sub10_dict=txt_to_dictkey("F:\software_code/近似计算\sample_test_gaussion\gnn_model/uint_lib/latency/sub10_dataset_latency.txt")
    #print(single_design)
    for idx,uint_design in enumerate(single_design):
        if idx <= 1:
            link_feature = [1, 0, 1] if uint_design in single_design_link else [1, 0, 0]
            add8_latency = list(eval(add8_dict.get(uint_design)))
            all_design_input.append(add8_latency + link_feature)
        elif 2 <= idx <= 3:
            link_feature = [1, 0, 1] if uint_design in single_design_link else [1, 0, 0]
            add12_latency = list(eval(add12_dict.get(uint_design)))
            all_design_input.append(add12_latency + link_feature)
        elif idx == 4:
            link_feature = [0, 1, 1] if uint_design in single_design_link else [0, 1, 0]
            sub10_latency = list(eval(sub10_dict.get(uint_design)))
            all_design_input.append(sub10_latency + link_feature)
    return torch.tensor(all_design_input)
def single_design_totensor_area_gaussion(single_design):
    all_design_input=[]
    mul8_area=txt_to_dictkey("F:\software_code/近似计算\sample_test_gaussion\gnn_model/uint_lib/area_power/mul8.txt")
    add16_area = txt_to_dictkey("F:\software_code/近似计算\sample_test_gaussion\gnn_model/uint_lib/area_power/add16.txt")
    for uint_design in single_design:
        if uint_design in mul8_area:
            mul_area_in=list(eval(mul8_area.get(uint_design)))
            new_mul_area_in=[x/300 for x in mul_area_in]
            all_design_input.append(new_mul_area_in+[1,0])
        else:
            add_area_in = list(eval(add16_area.get(uint_design)))
            new_add_area_in = [x / 100 for x in add_area_in]
            all_design_input.append(new_add_area_in+ [0, 1])
    return torch.tensor(all_design_input)
def single_design_totensor_power_gaussion(single_design):
    all_design_input=[]
    mul8_area=txt_to_dictkey("F:\software_code/近似计算\sample_test_gaussion\gnn_model/uint_lib/area_power/mul8.txt")
    add16_area = txt_to_dictkey("F:\software_code/近似计算\sample_test_gaussion\gnn_model/uint_lib/area_power/add16.txt")
    for uint_design in single_design:
        if uint_design in mul8_area:
            mul_area_in=list(eval(mul8_area.get(uint_design)))
            new_mul_area_in=[x/100 for x in mul_area_in]
            all_design_input.append(new_mul_area_in+[1,0])
        else:
            add_area_in = list(eval(add16_area.get(uint_design)))
            new_add_area_in = [x / 50 for x in add_area_in]
            all_design_input.append(new_add_area_in+ [0, 1])
    return torch.tensor(all_design_input)
def single_design_totensor_gaussion_ssim(single_design):
    all_design_input=[]
    mul8_dict=txt_to_dictkey("F:\software_code/近似计算\sample_test_gaussion\gnn_model/uint_lib/ssim/mul8.txt")
    add16_dict = txt_to_dictkey("F:\software_code/近似计算\sample_test_gaussion\gnn_model/uint_lib/ssim/add16.txt")
    for idx,uint_design in enumerate(single_design):
        if idx<=3:
            mul_ssim=list(eval(mul8_dict.get(uint_design)))
            mul_ssim=[mul_ssim[0]/150,mul_ssim[1]/100,mul_ssim[2],math.log10(mul_ssim[3])+2,math.log10(mul_ssim[4])+2,math.log10(mul_ssim[5])+2,math.log10(mul_ssim[6])+2]
            all_design_input.append(mul_ssim+[1,0,1,0,0])
        elif 4<=idx<=7:
            mul_ssim=list(eval(mul8_dict.get(uint_design)))
            mul_ssim=[mul_ssim[0]/150,mul_ssim[1]/100,mul_ssim[2],math.log10(mul_ssim[3])+2,math.log10(mul_ssim[4])+2,math.log10(mul_ssim[5])+2,math.log10(mul_ssim[6])+2]
            all_design_input.append(mul_ssim+[1,0,0,1,0])
        elif idx==8:
            mul_ssim=list(eval(mul8_dict.get(uint_design)))
            mul_ssim=[mul_ssim[0]/150,mul_ssim[1]/100,mul_ssim[2],math.log10(mul_ssim[3])+2,math.log10(mul_ssim[4])+2,math.log10(mul_ssim[5])+2,math.log10(mul_ssim[6])+2]
            all_design_input.append(mul_ssim+[1,0,0,0,1])
        elif 9<=idx<=12:
            add_ssim=list(eval(add16_dict.get(uint_design)))
            add_ssim = [add_ssim[0] / 50, add_ssim[1] / 50, add_ssim[2], math.log10(add_ssim[3]) + 2,math.log10(add_ssim[4]) + 2, math.log10(add_ssim[5]) + 2, math.log10(add_ssim[6]) +2]
            all_design_input.append(add_ssim+ [0,1,1,0,0])
        elif 13<=idx<=14:
            add_ssim=list(eval(add16_dict.get(uint_design)))
            add_ssim = [add_ssim[0] / 50, add_ssim[1] / 50, add_ssim[2], math.log10(add_ssim[3]) + 2,math.log10(add_ssim[4]) + 2, math.log10(add_ssim[5]) + 2, math.log10(add_ssim[6]) +2]
            all_design_input.append(add_ssim+ [0,1,0,1,0])
        elif 15<=idx<=16:
            add_ssim=list(eval(add16_dict.get(uint_design)))
            add_ssim = [add_ssim[0] / 50, add_ssim[1] / 50, add_ssim[2], math.log10(add_ssim[3]) + 2,math.log10(add_ssim[4]) + 2, math.log10(add_ssim[5]) + 2, math.log10(add_ssim[6]) +2]
            all_design_input.append(add_ssim+ [0,1,0,0,1])
    return torch.tensor(all_design_input)
def single_design_totensor_gaussion_node(single_design):
    all_design_input=[]
    mul8_dict=txt_to_dictkey("F:\software_code/近似计算\sample_test_gaussion\gnn_model/uint_lib/latency/mul8_dataset_latency.txt")
    add16_dict = txt_to_dictkey("F:\software_code/近似计算\sample_test_gaussion\gnn_model/uint_lib/latency/add16_dataset_latency.txt")
    for idx, uint_design in enumerate(single_design):
        if  idx < 8:
            mul_latency_in = list(eval(mul8_dict.get(uint_design)))
            all_design_input.append(mul_latency_in + [1, 0] + [1,0,0,0,0])
        elif  idx ==8:
            mul_latency_in = list(eval(mul8_dict.get(uint_design)))
            all_design_input.append(mul_latency_in + [1, 0] + [0,0,0,0,0])
        elif 9 <= idx <=12:
            add_latency_in = list(eval(add16_dict.get(uint_design)))
            all_design_input.append(add_latency_in + [0, 1] + [0,1,0,0,0])
        elif 13<=idx<=14:
            add_latency_in = list(eval(add16_dict.get(uint_design)))
            all_design_input.append(add_latency_in + [0, 1] + [0,0,1,0,0])
        elif idx==15:
            add_latency_in = list(eval(add16_dict.get(uint_design)))
            all_design_input.append(add_latency_in + [0, 1] + [0, 0, 0, 1,0])
        elif idx==16:
            add_latency_in = list(eval(add16_dict.get(uint_design)))
            all_design_input.append(add_latency_in + [0, 1] + [0, 0, 0, 0,1])
    return torch.tensor(all_design_input)
def single_design_totensor_gaussion_link(single_design,single_design_link):
    all_design_input=[]
    mul8_dict=txt_to_dictkey("F:\software_code/近似计算\sample_test_gaussion\gnn_model/uint_lib/latency/mul8_dataset_latency.txt")
    add16_dict = txt_to_dictkey("F:\software_code/近似计算\sample_test_gaussion\gnn_model/uint_lib/latency/add16_dataset_latency.txt")
    for uint_design in single_design:
        if uint_design in mul8_dict:
            link_feature=[1,0,1] if uint_design in single_design_link else [1,0,0]
            mul_latency_in=list(eval(mul8_dict.get(uint_design)))
            all_design_input.append(mul_latency_in+link_feature)
        else:
            link_feature = [0, 1, 1] if uint_design in single_design_link else [0, 1, 0]
            add_latency_in=list(eval(add16_dict.get(uint_design)))
            all_design_input.append(add_latency_in+link_feature)
    return torch.tensor(all_design_input)
def single_design_totensor_kmeans_area(single_design):
    all_design_input=[]
    mul8_area_dict=txt_to_dictkey("F:\software_code\近似计算\sample_test_gaussion\gnn_model/uint_lib/area_power/kmeans/pre_pruning_mul8.txt")
    mul11_area_dict=txt_to_dictkey("F:\software_code\近似计算\sample_test_gaussion\gnn_model/uint_lib/area_power/kmeans/pre_pruning_mul11.txt")
    sub10_area_dict=txt_to_dictkey("F:\software_code\近似计算\sample_test_gaussion\gnn_model/uint_lib/area_power/kmeans/pre_pruning_sub10.txt")
    add16_area_dict=txt_to_dictkey("F:\software_code\近似计算\sample_test_gaussion\gnn_model/uint_lib/area_power/kmeans/pre_pruning_add16.txt")
    #print(single_design)
    for uint_design in single_design:
        if uint_design in sub10_area_dict:
            sub_area_in=list(eval(sub10_area_dict.get(uint_design)))
            new_sub_area_in=[x/30 for x in sub_area_in[:2]]
            all_design_input.append(new_sub_area_in+[1,0])
        elif uint_design in mul8_area_dict:
            mul8_area_in = list(eval(mul8_area_dict.get(uint_design)))
            new_mul8_area_in = [x / 200 for x in mul8_area_in[:2]]
            all_design_input.append(new_mul8_area_in+ [0, 1])
        elif uint_design in add16_area_dict:
            add16_area_in = list(eval(add16_area_dict.get(uint_design)))
            new_add16_area_in = [x / 50 for x in add16_area_in[:2]]
            all_design_input.append(new_add16_area_in + [1,0])
        elif uint_design in mul11_area_dict:
            mul11_area_in = list(eval(mul11_area_dict.get(uint_design)))
            new_mul11_area_in = [x / 400 for x in mul11_area_in[:2]]
            all_design_input.append(new_mul11_area_in + [0, 1])
    img_mem=[1.08,0.13,0,0]
    clust_mem=[1.085,0.131,0,0]
    contorl=[1.1,0.477,0,0]
    sum_mem=[1.085,0.131,0,0]
    ave_div=[1.0746,1.04,0,0]
    new_clust=[1.085,0.131,0,0]
    add17=[0.7,0.36,1,0]
    new_design_input=[img_mem]+[clust_mem]+all_design_input[:7]+[add17]+all_design_input[7:15]+[add17]+[all_design_input[15]]+[contorl]+[sum_mem]+[ave_div]+[new_clust]
    return torch.tensor(new_design_input)
def single_design_totensor_kmeans_power(single_design):
    all_design_input=[]
    mul8_area_dict = txt_to_dictkey("F:\software_code\近似计算\sample_test_gaussion\gnn_model/uint_lib/area_power/kmeans/pre_pruning_mul8.txt")
    mul11_area_dict = txt_to_dictkey("F:\software_code\近似计算\sample_test_gaussion\gnn_model/uint_lib/area_power/kmeans/pre_pruning_mul11.txt")
    sub10_area_dict = txt_to_dictkey("F:\software_code\近似计算\sample_test_gaussion\gnn_model/uint_lib/area_power/kmeans/pre_pruning_sub10.txt")
    add16_area_dict = txt_to_dictkey("F:\software_code\近似计算\sample_test_gaussion\gnn_model/uint_lib/area_power/kmeans/pre_pruning_add16.txt")
    #print(single_design)
    for uint_design in single_design:
        if uint_design in sub10_area_dict:
            sub_area_in=list(eval(sub10_area_dict.get(uint_design)))
            new_sub_area_in=[x/20 for x in sub_area_in[:2]]
            all_design_input.append(new_sub_area_in+[1,0])
        elif uint_design in mul8_area_dict:
            mul8_area_in = list(eval(mul8_area_dict.get(uint_design)))
            new_mul8_area_in = [x / 200 for x in mul8_area_in[:2]]
            all_design_input.append(new_mul8_area_in+ [0, 1])
        elif uint_design in add16_area_dict:
            add16_area_in = list(eval(add16_area_dict.get(uint_design)))
            new_add16_area_in = [x / 20 for x in add16_area_in[:2]]
            all_design_input.append(new_add16_area_in + [1,0])
        elif uint_design in mul11_area_dict:
            mul11_area_in = list(eval(mul11_area_dict.get(uint_design)))
            new_mul11_area_in = [x / 300 for x in mul11_area_in[:2]]
            all_design_input.append(new_mul11_area_in + [0, 1])
    img_mem=[1.08,0.13,0,0]
    clust_mem=[1.085,0.131,0,0]
    contorl=[1.1,0.477,0,0]
    sum_mem=[1.085,0.131,0,0]
    ave_div=[1.0746,1.04,0,0]
    new_clust=[1.085,0.131,0,0]
    add17=[0.7,0.36,1,0]
    new_design_input=[img_mem]+[clust_mem]+all_design_input[:7]+[add17]+all_design_input[7:15]+[add17]+[all_design_input[15]]+[contorl]+[sum_mem]+[ave_div]+[new_clust]
    return torch.tensor(new_design_input)
def single_design_totensor_kmeans_ssim(single_design):
    all_design_input=[]
    mul8_area_dict = txt_to_dictkey("F:\software_code\近似计算\sample_test_gaussion\gnn_model/uint_lib/ssim/kmeans/pre_pruning_mul8.txt")
    mul11_area_dict = txt_to_dictkey("F:\software_code\近似计算\sample_test_gaussion\gnn_model/uint_lib/ssim/kmeans/pre_pruning_mul11.txt")
    sub10_area_dict = txt_to_dictkey("F:\software_code\近似计算\sample_test_gaussion\gnn_model/uint_lib/ssim/kmeans/pre_pruning_sub10.txt")
    add16_area_dict = txt_to_dictkey("F:\software_code\近似计算\sample_test_gaussion\gnn_model/uint_lib/ssim/kmeans/pre_pruning_add16.txt")
    for uint_design in single_design:
        if uint_design in sub10_area_dict:
            sub_area_in = list(eval(sub10_area_dict.get(uint_design)))
            new_sub_area_in = [sub_area_in[0] / 30, sub_area_in[1] / 30, sub_area_in[2],
                               (math.log10(sub_area_in[3]) + 2) / 5, (math.log10(sub_area_in[4]) + 2) / 5,
                               (math.log10(sub_area_in[5]) + 2) / 5, (math.log10(sub_area_in[6]) + 2) / 5]
            all_design_input.append(new_sub_area_in + [1, 0, 0])
        elif uint_design in mul8_area_dict:
            mul8_area_in = list(eval(mul8_area_dict.get(uint_design)))
            new_mul8_area_in = [mul8_area_in[0] / 200, mul8_area_in[1] / 200, mul8_area_in[2],
                                (math.log10(mul8_area_in[3]) + 2) / 5, (math.log10(mul8_area_in[4]) + 2) / 5,
                                (math.log10(mul8_area_in[5]) + 2) / 5, (math.log10(mul8_area_in[6]) + 2) / 5]
            all_design_input.append(new_mul8_area_in + [0, 1, 0])
        elif uint_design in add16_area_dict:
            add16_area_in = list(eval(add16_area_dict.get(uint_design)))
            new_add16_area_in = [add16_area_in[0] / 50, add16_area_in[1] / 50, add16_area_in[2],
                                 (math.log10(add16_area_in[3]) + 2) / 5, (math.log10(add16_area_in[4]) + 2) / 5,
                                 (math.log10(add16_area_in[5]) + 2) / 5, (math.log10(add16_area_in[6]) + 2) / 5]
            all_design_input.append(new_add16_area_in + [0, 0, 1])
    add17 = [0.7, 0.36, 0.6, 0, 0, 0, 0, 0, 0, 1]
    zero_list = [0] * 10
    dif_compute_core = [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0],
                        [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0],
                        [0, 0, 1]]
    new_design_input = all_design_input[:7] + [add17] + all_design_input[7:14] + [add17] + [zero_list]
    new_design_input = torch.cat((torch.tensor(new_design_input), torch.tensor(dif_compute_core)), dim=1)
    return new_design_input
def single_design_totensor_kmeans_node(single_design):
    all_design_input=[]
    sub10_dataset_latency=txt_to_dictkey("F:\software_code\近似计算\sample_test_gaussion\gnn_model/uint_lib/latency/kmeans/sub10_dataset_latency.txt")
    mul8_dataset_latency=txt_to_dictkey("F:\software_code\近似计算\sample_test_gaussion\gnn_model/uint_lib/latency/kmeans/mul8_dataset_latency.txt")
    add16_dataset_latency=txt_to_dictkey("F:\software_code\近似计算\sample_test_gaussion\gnn_model/uint_lib/latency/kmeans/add16_dataset_latency.txt")
    mul11_dataset_latency=txt_to_dictkey("F:\software_code\近似计算\sample_test_gaussion\gnn_model/uint_lib/latency/kmeans/mul11_dataset_latency.txt")
    for idx, uint_design in enumerate(single_design):
        if  uint_design in sub10_dataset_latency.keys():
            sub10_latency_in = list(eval(sub10_dataset_latency.get(uint_design)))
            #mul_area_in = list(eval(mul8_area.get(uint_design)))
            #mul8_one_hot_in = list(eval(mul8_one_hot.get(uint_design)))
            #new_mul_area_in = [x / 300 for x in mul_area_in]
            all_design_input.append(sub10_latency_in + [1, 0] + [1,0,0,0,0])
        elif  uint_design in mul8_dataset_latency:
            mul_latency_in = list(eval(mul8_dataset_latency.get(uint_design)))
            #mul_area_in = list(eval(mul8_area.get(uint_design)))
            #mul8_one_hot_in = list(eval(mul8_one_hot.get(uint_design)))
            #new_mul_area_in = [x / 300 for x in mul_area_in]
            all_design_input.append(mul_latency_in + [1, 0] + [0,1,0,0,0])
        elif uint_design in add16_dataset_latency:
            add16_latency_in = list(eval(add16_dataset_latency.get(uint_design)))
            #add_area_in = list(eval(add16_area.get(uint_design)))
            #add16_one_hot_in = list(eval(add16_one_hot.get(uint_design)))
            #new_add_area_in = [x / 100 for x in add_area_in]
            all_design_input.append(add16_latency_in + [0, 1] + [0,0,1,0,0])
        elif uint_design in mul11_dataset_latency:
            mul11_latency_in = list(eval(mul11_dataset_latency.get(uint_design)))
            #add_area_in = list(eval(add16_area.get(uint_design)))
            #add16_one_hot_in = list(eval(add16_one_hot.get(uint_design)))
            #new_add_area_in = [x / 100 for x in add_area_in]
            all_design_input.append(mul11_latency_in + [0, 1] + [0,0,0,1,0])
    zero_list_add17=[0]*16+ [0,0,0,1,0]
    zero_list_all=[0]*16+[0,0,0,0,1]
    new_design_input=all_design_input[:7]+[zero_list_add17]+all_design_input[7:15]+[zero_list_add17]+[all_design_input[15]]+[zero_list_all]
    return torch.tensor(new_design_input)
def single_design_totensor_kmeans_latency(single_design,single_design_link):
    all_design_input = []
    sub10_dataset_latency = txt_to_dictkey("F:\software_code\近似计算\sample_test_gaussion\gnn_model/uint_lib/latency/kmeans/sub10_dataset_latency.txt")
    mul8_dataset_latency = txt_to_dictkey("F:\software_code\近似计算\sample_test_gaussion\gnn_model/uint_lib/latency/kmeans/mul8_dataset_latency.txt")
    add16_dataset_latency = txt_to_dictkey("F:\software_code\近似计算\sample_test_gaussion\gnn_model/uint_lib/latency/kmeans/add16_dataset_latency.txt")
    mul11_dataset_latency = txt_to_dictkey("F:\software_code\近似计算\sample_test_gaussion\gnn_model/uint_lib/latency/kmeans/mul11_dataset_latency.txt")
    for idx, uint_design in enumerate(single_design):
        if uint_design in sub10_dataset_latency.keys():
            sub10_latency_in = list(eval(sub10_dataset_latency.get(uint_design)))
            all_design_input.append(sub10_latency_in + [1, 0] )
        elif uint_design in mul8_dataset_latency:
            mul_latency_in = list(eval(mul8_dataset_latency.get(uint_design)))
            all_design_input.append(mul_latency_in + [0, 1] )
        elif uint_design in add16_dataset_latency:
            add16_latency_in = list(eval(add16_dataset_latency.get(uint_design)))
            all_design_input.append(add16_latency_in + [1, 0] )
        elif uint_design in mul11_dataset_latency:
            mul11_latency_in = list(eval(mul11_dataset_latency.get(uint_design)))
            all_design_input.append(mul11_latency_in + [0, 1] )
    zero_list = [0] * 16
    new_design_input = all_design_input[:7] + [zero_list] + all_design_input[7:15] + [zero_list] + [all_design_input[15]] + [zero_list]
    import_idx = torch.zeros(19)
    import_idx[single_design_link] = 1
    final_tensor=torch.cat((torch.tensor(new_design_input),import_idx.unsqueeze(1)),dim=1)
    return final_tensor