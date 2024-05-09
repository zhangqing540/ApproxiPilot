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
        edge_index = torch.tensor([[0, 9, 1, 9, 2, 10, 3, 10, 4, 11, 5, 11, 6, 12, 7, 12, 8, 16, 9, 13, 10, 13, 11, 14,
                                    12, 14, 13, 15, 14, 15, 15, 16],
                                   [9, 0, 9, 1, 10, 2, 10, 3, 11, 4, 11, 5, 12, 6, 12, 7, 16, 8, 13, 9, 13, 10, 14, 11,
                                    14, 12, 15, 13, 15, 14, 16, 15]], dtype=torch.long, device=device)
        input_file= "dataset/train.txt"
        all_design_name,all_latency,all_design_link=design_name_and_value(input_file)
        for single_input_name,single_latency,single_design_link in zip(all_design_name,all_latency,all_design_link):
            single_input_data=single_design_totensor(single_input_name,single_design_link)
            data=Data(x=single_input_data,edge_index=edge_index,y=torch.tensor(float(single_latency)))
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
        edge_index = torch.tensor([[0, 9, 1, 9, 2, 10, 3, 10, 4, 11, 5, 11, 6, 12, 7, 12, 8, 16, 9, 13, 10, 13, 11, 14,
                                    12, 14, 13, 15, 14, 15, 15, 16],
                                   [9, 0, 9, 1, 10, 2, 10, 3, 11, 4, 11, 5, 12, 6, 12, 7, 16, 8, 13, 9, 13, 10, 14, 11,
                                    14, 12, 15, 13, 15, 14, 16, 15]], dtype=torch.long, device=device)
        input_file = "dataset/test.txt"
        all_design_name, all_latency, all_design_link = design_name_and_value(input_file)
        for single_input_name, single_latency, single_design_link in zip(all_design_name, all_latency, all_design_link):
            single_input_data = single_design_totensor(single_input_name, single_design_link)
            data = Data(x=single_input_data, edge_index=edge_index, y=torch.tensor(float(single_latency)))
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
    all_latency=[]
    all_design_link=[]
    with open(path,"r")as file:
        lines=file.readlines()
    for design in lines:
        all_design_feature=design[:-1].split(" ")
        all_design_name.append(all_design_feature[:17])
        all_latency.append(float(all_design_feature[17]))
        all_design_link.append(all_design_feature[18:])
    return all_design_name,all_latency,all_design_link
def single_design_totensor(single_design,single_design_link):
    all_design_input=[]
    mul8_dict=txt_to_dictkey("pruning_lib/mul8_dataset_latency.txt")
    add16_dict = txt_to_dictkey("pruning_lib/add16_dataset_latency.txt")
    mul8_area=txt_to_dictkey("pruning_lib/area/mul8.txt")
    add16_area = txt_to_dictkey("pruning_lib/area/add16.txt")
    mul8_one_hot=txt_to_dictkey("pruning_lib/one_hot/mul8.txt")
    add16_one_hot = txt_to_dictkey("pruning_lib/one_hot/add16.txt")
    #print(single_design)
    for uint_design in single_design:
        if uint_design in mul8_dict:
            link_feature=[1,0,1] if uint_design in single_design_link else [1,0,0]
            mul_latency_in=list(eval(mul8_dict.get(uint_design)))
            mul_area_in=list(eval(mul8_area.get(uint_design)))
            mul8_one_hot_in=list(eval(mul8_one_hot.get(uint_design)))
            new_mul_area_in=[x/300 for x in mul_area_in]
            all_design_input.append(mul_latency_in+link_feature)
        else:
            link_feature = [0, 1, 1] if uint_design in single_design_link else [0, 1, 0]
            add_latency_in=list(eval(add16_dict.get(uint_design)))
            add_area_in = list(eval(add16_area.get(uint_design)))
            add16_one_hot_in = list(eval(add16_one_hot.get(uint_design)))
            new_add_area_in = [x / 100 for x in add_area_in]
            all_design_input.append(add_latency_in+link_feature)
    return torch.tensor(all_design_input)