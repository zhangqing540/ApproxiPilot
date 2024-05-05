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
        edge_index=torch.tensor([[0,1,2,3],[2,3,4,4]],dtype=torch.long,device=device)
        input_file= "dataset/sobel/deepapprox_sobel_3.6w_train.txt"
        node_name,label_list=read_file(input_file)
        for idx in range(len(label_list)):
            x=node_feature(node_name[idx])
            label=torch.tensor(label_list[idx],dtype=torch.float32)
            #print(label)
            data=Data(x=x,edge_index=edge_index,y=label)
            #data = Data(x=x, edge_index=edge_index, y=y)
            data_list.append(data)
        data, slices = self.collate(data_list)
        torch.save((data, slices), self.processed_paths[0])
class test_dataset(InMemoryDataset):
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
        edge_index=torch.tensor([[0,1,2,3],[2,3,4,4]],dtype=torch.long,device=device)
        input_file= "dataset/sobel/deepapprox_sobel_4k_test.txt"
        node_name,label_list=read_file(input_file)
        for idx in range(len(label_list)):
            x=node_feature(node_name[idx])
            label=torch.tensor(label_list[idx],dtype=torch.float32,device=device)
            data=Data(x=x,edge_index=edge_index,y=label)
            #data = Data(x=x, edge_index=edge_index, y=y)
            data_list.append(data)
        data, slices = self.collate(data_list)
        torch.save((data, slices), self.processed_paths[0])
def read_file(file_name):
    data = []
    node_name=[]
    with open(file_name, 'r') as file:
        for line in file:
            numbers = line.strip().split(" ")
            #print(numbers)
            name=numbers[0]+" "+numbers[1]+" "+numbers[2]+" "+numbers[3]+" "+numbers[4]
            area=numbers[5]
            power=numbers[6]
            latency=numbers[7]
            ssim=numbers[8]
            #link=ast.literal_eval(numbers[-1])
            one_data = [float(latency)]
            #one_data=[float(area[5:]),float(power[6:]),float(latency[8:]),float(ssim[5:])]
            #print("one", one_data)
            data.append(one_data)
            #print("data",data)
            node_name.append(name)
            #link_lib.append(link)
            #print(link)
    return node_name,data
def read_file_sample(file_name):
    node_name=[]
    with open(file_name, 'r') as file:
        for line in file:
            numbers = line.strip().split()
            #print("num",numbers )
            name=numbers[0]+" "+numbers[1]+" "+numbers[2]+" "+numbers[3]+" "+numbers[4]
            node_name.append(name)
    return node_name
def node_feature(input_feature):
    add8_uint_lib_change = {}
    add12_uint_lib_change = {}
    sub10_uint_lib_change = {}
    add8_uint_lib_ori = {}
    add12_uint_lib_ori = {}
    sub10_uint_lib_ori = {}
    add8_pruning_path = "pruning_lib/unit_latency/add8_latency.txt"
    add12_pruning_path = "pruning_lib/unit_latency/add12_latency.txt"
    sub10_pruning_path = "pruning_lib/unit_latency/sub10_latency.txt"
    add8_pruning = "pruning_lib/uint_basic/add8.txt"
    add12_pruning = "pruning_lib/uint_basic/add12.txt"
    sub10_pruning = "pruning_lib/uint_basic/sub10.txt"
    add81, add82, add91, add92, sub101 = input_feature.split()
    with open(add8_pruning_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            key, value = line.strip().split(': ')
            add8_uint_lib_change[key] = ast.literal_eval(value)
    with open(add12_pruning_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            key, value= line.strip().split(': ')
            add12_uint_lib_change[key] = ast.literal_eval(value)
    with open(sub10_pruning_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            key, value= line.strip().split(': ')
            sub10_uint_lib_change[key] =ast.literal_eval(value)
    feature81_change = add8_uint_lib_change.get(add81)
    feature82_change = add8_uint_lib_change.get(add82)
    feature91_change = add12_uint_lib_change.get(add91)
    feature92_change = add12_uint_lib_change.get(add92)
    feature10_change = sub10_uint_lib_change.get(sub101)
    #print(feature81_change,feature82_change,feature91_change,feature92_change,feature10_change)
    #exit()
    with open(add8_pruning, 'r') as file:
        lines = file.readlines()
        for line in lines:
            key, value = line.strip().split(': ')
            add8_uint_lib_ori[key] = ast.literal_eval(value)
    with open(add12_pruning, 'r') as file:
        lines = file.readlines()
        for line in lines:
            key, value = line.strip().split(': ')
            add12_uint_lib_ori[key] = ast.literal_eval(value)
    with open(sub10_pruning, 'r') as file:
        lines = file.readlines()
        for line in lines:
            key, value = line.strip().split(': ')
            #print(key,len(ast.literal_eval(value)))
            sub10_uint_lib_ori[key] = ast.literal_eval(value)
    feature81_ori = add8_uint_lib_ori.get(add81)
    feature82_ori = add8_uint_lib_ori.get(add82)
    feature91_ori = add12_uint_lib_ori.get(add91)
    feature92_ori = add12_uint_lib_ori.get(add92)
    feature10_ori = sub10_uint_lib_ori.get(sub101)
    #print(feature81_ori,feature82_ori,feature91_ori,feature92_ori,feature10_ori)
    new_feature81=feature81_change+feature81_ori
    new_feature82 = feature82_change + feature82_ori
    new_feature91 = feature91_change + feature91_ori
    new_feature92 = feature92_change +feature92_ori
    new_feature10 = feature10_change +feature10_ori
    node_feature=np.array([new_feature81,new_feature82,new_feature91,new_feature92,new_feature10])
    #print(node_feature)
    #exit(0)
    node_feature=torch.from_numpy(node_feature).to(torch.float32)
    return node_feature.to(device)
