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
        edge_index=graph_link("dataset/link/part_link.txt")
        input_file= "dataset/train.txt"
        all_design_name,all_link=design_name_and_value(input_file)
        for single_input_name,single_link in zip(all_design_name,all_link):
            single_input_data=single_design_totensor(single_input_name)
            output_label=classfication_label(single_input_name,single_link)
            data=Data(x=single_input_data,edge_index=edge_index,y=output_label)
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
        data_list = []
        edge_index = graph_link("dataset/link/part_link.txt")
        input_file = "dataset/test.txt"
        all_design_name, all_link = design_name_and_value(input_file)
        for single_input_name, single_link in zip(all_design_name, all_link):
            single_input_data = single_design_totensor(single_input_name)
            output_label = classfication_label(single_input_name, single_link)
            data = Data(x=single_input_data, edge_index=edge_index, y=output_label)
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
    #print("data")
    all_design_name=[]
    all_design_link=[]
    with open(path,"r")as file:
        lines=file.read().rstrip('\n').splitlines()
    for design in lines:
        all_design_feature=design.split(" ")
        all_design_name.append(all_design_feature[:16])
        all_design_link.append(all_design_feature[17:])
    return all_design_name,all_design_link
def single_design_totensor(single_design):
    all_design_input=[]
    sub10_dataset_latency=txt_to_dictkey("uint_lib/sub10_dataset_latency.txt")
    mul8_dataset_latency=txt_to_dictkey("uint_lib/mul8_dataset_latency.txt")
    add16_dataset_latency=txt_to_dictkey("uint_lib/add16_dataset_latency.txt")
    mul11_dataset_latency=txt_to_dictkey("uint_lib/mul11_dataset_latency.txt")
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
def classfication_label(single_input_name,single_link):
    classification_label=0
    if single_link[2]=="add17":
        new_link=[single_link[0],single_link[1],single_link[3]]
        target_link=[[single_input_name[2],single_input_name[5],single_input_name[7]],[single_input_name[10],single_input_name[13],single_input_name[15]]]
        if new_link==target_link[0]:classification_label = [2, 5, 7, 8, 18]
        elif new_link==target_link[1]:classification_label = [11, 14, 16, 17, 18]
        else:print("error")
    else:
        target_link=[[single_input_name[0],single_input_name[3],single_input_name[6],single_input_name[7]],
                     [single_input_name[1],single_input_name[4],single_input_name[6],single_input_name[7]],
                     [single_input_name[8],single_input_name[11],single_input_name[14],single_input_name[15]],
                     [single_input_name[9],single_input_name[12],single_input_name[14],single_input_name[15]]]
        if single_link==target_link[0]:classification_label =[0,3,6,7,8,18]
        elif single_link==target_link[1]:classification_label =[1,4,6,7,8,18]
        elif single_link == target_link[2]:classification_label = [9, 12, 15, 16, 17,18]
        elif single_link == target_link[3]:classification_label = [10,13,15,16,17,18]
        else:print("error")
    if classification_label==0:
        print(single_link)
        print(single_input_name)
        exit()
    output_label = np.zeros(19)
    output_label[classification_label] = 1
    return torch.tensor(output_label)