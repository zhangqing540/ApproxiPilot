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
        edge_index = torch.tensor([[0, 2, 1, 3, 2, 4, 3, 4],
                                   [2, 0, 3, 1, 4, 2, 4, 3]], dtype=torch.long, device=device)
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
        edge_index = torch.tensor([[0, 2, 1, 3, 2, 4, 3, 4],
                                   [2, 0, 3, 1, 4, 2, 4, 3]], dtype=torch.long, device=device)
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
        lines=file.read().rstrip('\n').splitlines()
    for design in lines:
        all_design_feature=design.split(" ")
        all_design_name.append(all_design_feature[:5])
        all_area.append(float(all_design_feature[-1]))
    return all_design_name,all_area
def single_design_totensor(single_design):
    all_design_input=[]
    add8_dict=txt_to_dictkey("pruning_lib/add8.txt")
    add12_dict = txt_to_dictkey("pruning_lib/add12.txt")
    sub10_dict=txt_to_dictkey("pruning_lib/sub10.txt")
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