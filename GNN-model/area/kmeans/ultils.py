import torch
from torch_geometric.data import InMemoryDataset,Data
import numpy as np
import torch.nn.functional as F
import ast
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
node_feature_num=50
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
        edge_index=graph_link("dataset/link/link.txt")
        input_file= "dataset/train.txt"
        all_design_name,all_area=design_name_and_value(input_file)
        for single_input_name,single_area in zip(all_design_name,all_area):
            single_input_data=single_design_totensor(single_input_name)
            data=Data(x=single_input_data,edge_index=edge_index,y=torch.tensor(single_area))
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
        edge_index = graph_link("dataset/link/link.txt")
        input_file = "dataset/test.txt"
        all_design_name, all_area = design_name_and_value(input_file)
        for single_input_name, single_area in zip(all_design_name, all_area):
            single_input_data = single_design_totensor(single_input_name)
            data = Data(x=single_input_data, edge_index=edge_index, y=torch.tensor(single_area))
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
    all_area=[]
    with open(path,"r")as file:
        lines=file.readlines()
    for design in lines:
        all_design_feature=design[:-1].split(" ")
        all_design_name.append(all_design_feature[:16])
        all_area.append(float(all_design_feature[-1]))
    return all_design_name,all_area
def single_design_totensor(single_design):
    all_design_input=[]
    mul8_area_dict=txt_to_dictkey("pruning_lib/pre_pruning_mul8.txt")
    mul11_area_dict=txt_to_dictkey("pruning_lib/pre_pruning_mul11.txt")
    sub10_area_dict=txt_to_dictkey("pruning_lib/pre_pruning_sub10.txt")
    add16_area_dict=txt_to_dictkey("pruning_lib/pre_pruning_add16.txt")
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