import torch
from torch_geometric.data import InMemoryDataset,Data
import numpy as np
import torch.nn.functional as F
import ast
import math
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
class train_dataset(InMemoryDataset):
    def __init__(self, root, transform=None, pre_transform=None, pre_filter=None):
        super().__init__(root, transform, pre_transform, pre_filter)
        self.data, self.slices = torch.load(self.processed_paths[0])

    @property
    def raw_file_names(self):
        return [ ]

    @property
    def processed_file_names(self):
        return ['data.pt']

    def download(self):
        pass

    def process(self):
        # Read data into huge `Data` list.
        data_list = []
        edge_index = graph_link("dataset/link/part_link.txt")
        input_file= "dataset/train.txt"
        all_design_name,all_ssim=design_name_and_value(input_file)
        for single_input_name,single_ssim in zip(all_design_name,all_ssim):
            single_input_data=single_design_totensor(single_input_name)
            data=Data(x=single_input_data,edge_index=edge_index,y=torch.tensor(single_ssim))
            data_list.append(data)
        data, slices = self.collate(data_list)
        torch.save((data, slices), self.processed_paths[0])
class test_dataset(InMemoryDataset):
    def __init__(self, root, transform=None, pre_transform=None, pre_filter=None):
        super().__init__(root, transform, pre_transform, pre_filter)
        self.data, self.slices = torch.load(self.processed_paths[0])

    @property
    def raw_file_names(self):
        return []

    @property
    def processed_file_names(self):
        return ['data.pt']

    def download(self):
        pass

    def process(self):
        # Read data into huge `Data` list.
        data_list = []
        edge_index = graph_link("dataset/link/part_link.txt")
        input_file = "dataset/test.txt"
        all_design_name, all_ssim = design_name_and_value(input_file)
        for single_input_name, single_ssim in zip(all_design_name, all_ssim):
            single_input_data = single_design_totensor(single_input_name)

            data = Data(x=single_input_data, edge_index=edge_index, y=torch.tensor(single_ssim))
            data_list.append(data)
        data, slices = self.collate(data_list)
        torch.save((data, slices), self.processed_paths[0])
def txt_to_dictkey(path):
    dict={}
    with open(path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            key, value = line.strip().split(': ')
            dict[key] =value
    return dict
def design_name_and_value(path):
    all_design_name=[]
    all_power=[]
    with open(path,"r")as file:
        lines=file.read().rstrip('\n').splitlines()
    for design in lines:
        all_design_feature=design.split(" ")
        all_design_name.append(all_design_feature[:16])
        all_power.append(float(all_design_feature[-1]))
    return all_design_name,all_power
def single_design_totensor(single_design):
    all_design_input=[]
    mul8_area_dict = txt_to_dictkey("pruning_lib/pre_pruning_mul8.txt")
    mul11_area_dict = txt_to_dictkey("pruning_lib/pre_pruning_mul11.txt")
    sub10_area_dict = txt_to_dictkey("pruning_lib/pre_pruning_sub10.txt")
    add16_area_dict = txt_to_dictkey("pruning_lib/pre_pruning_add16.txt")
    for uint_design in single_design:
        if uint_design in sub10_area_dict:
            sub_area_in = list(eval(sub10_area_dict.get(uint_design)))
            new_sub_area_in = [sub_area_in[0]/30,sub_area_in[1]/30,sub_area_in[2],(math.log10(sub_area_in[3])+2)/5,(math.log10(sub_area_in[4])+2)/5,(math.log10(sub_area_in[5])+2)/5,(math.log10(sub_area_in[6])+2)/5]
            all_design_input.append(new_sub_area_in + [1, 0,0,0])
        elif uint_design in mul8_area_dict:
            mul8_area_in = list(eval(mul8_area_dict.get(uint_design)))
            new_mul8_area_in = [mul8_area_in[0]/200,mul8_area_in[1]/200,mul8_area_in[2],(math.log10(mul8_area_in[3])+2)/5,(math.log10(mul8_area_in[4])+2)/5,(math.log10(mul8_area_in[5])+2)/5,(math.log10(mul8_area_in[6])+2)/5]
            all_design_input.append(new_mul8_area_in + [0, 1,0,0])
        elif uint_design in add16_area_dict:
            add16_area_in = list(eval(add16_area_dict.get(uint_design)))
            new_add16_area_in = [add16_area_in[0]/50,add16_area_in[1]/50,add16_area_in[2],(math.log10(add16_area_in[3])+2)/5,(math.log10(add16_area_in[4])+2)/5,(math.log10(add16_area_in[5])+2)/5,(math.log10(add16_area_in[6])+2)/5]
            all_design_input.append(new_add16_area_in + [0,0,1,0])
        elif uint_design in mul11_area_dict:
            mul11_area_in = list(eval(mul11_area_dict.get(uint_design)))
            new_mul11_area_in = [mul11_area_in[0] / 400, mul11_area_in[1] / 400, mul11_area_in[2],(math.log10(mul11_area_in[3]) + 2)/5,(math.log10(mul11_area_in[4]) + 2)/5,(math.log10(mul11_area_in[5]) + 2)/5,(math.log10(mul11_area_in[6]) + 2)/5]
            all_design_input.append(new_mul11_area_in + [0,0,0,1])
    add17=[0.7,0.36,0.6,0,0,0,0,0,0,1,0]
    zero_list = [0] * 11
    new_design_input = all_design_input[:7] + [add17] + all_design_input[7:15] + [add17] + [all_design_input[15]] + [zero_list]
    dif_compute_core=[[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,0,1]]
    #print(torch.tensor(new_design_input))
    #print(torch.tensor(dif_compute_core).shape)
    #exit()
    new_design_input=torch.cat((torch.tensor(new_design_input),torch.tensor(dif_compute_core)),dim=1)
    return new_design_input
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