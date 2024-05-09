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
        edge_index=graph_link("dataset/part_link.txt")
        input_file= "dataset/train.txt"
        all_design_name,all_latency,all_design_link=design_name_and_value(input_file)
        for single_input_name,single_latency,single_design_link in zip(all_design_name,all_latency,all_design_link):
            single_input_data=single_design_totensor(single_input_name,torch.tensor(list(map(float,single_design_link)),dtype=torch.long))
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
        edge_index = graph_link("dataset/part_link.txt")
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
        all_design_name.append(all_design_feature[:16])
        all_latency.append(float(all_design_feature[16]))
        all_design_link.append(all_design_feature[17:])
    return all_design_name,all_latency,all_design_link
def single_design_totensor(single_design,single_design_link):
    all_design_input = []
    sub10_dataset_latency = txt_to_dictkey("pruning_lib/sub10_dataset_latency.txt")
    mul8_dataset_latency = txt_to_dictkey("pruning_lib/mul8_dataset_latency.txt")
    add16_dataset_latency = txt_to_dictkey("pruning_lib/add16_dataset_latency.txt")
    mul11_dataset_latency = txt_to_dictkey("pruning_lib/mul11_dataset_latency.txt")
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
    final_tensor = torch.cat((torch.tensor(new_design_input), import_idx.unsqueeze(1)), dim=1)
    return final_tensor
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