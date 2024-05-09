import random
from gnn_model.test_sample_sobel import *
import pandas as pd
import numpy as np
import torch
import joblib
import copy
input_area=[]
output_area=[]
input_power=[]
output_power=[]
input_latency=[]
output_latency=[]
input_ssim=[]
output_ssim=[]
dataset_area= "RF_data/gaussion/area.txt"
dataset_power= "RF_data/gaussion/power.txt"
dataset_latency= "RF_data/gaussion/latency.txt"
dataset_ssim= "RF_data/gaussion/ssim.txt"
mul11_name=["mul11u_03N", "mul11u_097", "mul11u_01Z", "mul11u_067", "mul11u_05D","mul11u_00H", "mul11u_003", "mul11u_041", "mul11u_00K", "mul11u_024","mul11u_09Z"]
mul8_name=["mul8u_17R6", "mul8u_17C8", "mul8u_R36", "mul8u_T83","mul8u_874","mul8u_197B", "mul8u_2NDH", "mul8u_Z9D", "mul8u_L93","mul8u_17MJ", "mul8u_4X5", "mul8u_12KA", "mul8u_18UH","mul8u_19XF", "mul8u_ZDF", "mul8u_GTR", "mul8u_1JJQ","mul8u_1A0M", "mul8u_8U3", "mul8u_ZB3"]
add16_name=["add16u_0U8", "add16u_0KU", "add16u_0GX", "add16u_0PT", "add16u_0K3","add16u_0HK", "add16u_0EZ", "add16u_08V", "add16u_1A5", "add16u_126","add16u_0SL", "add16u_0J3", "add16u_162", "add16u_110", "add16u_15Q","add16u_067", "add16u_0SD", "add16u_0KG", "add16u_0RJ", "add16u_0NL"]
sub10_name=["sub10_90","sub10_260","sub10_1","sub10_130","sub10_270","sub10_15","sub10_135","sub10_5","sub10_210","sub10_26","sub10_6","sub10_85","sub10_200"]
init_set=random.sample(sub10_name,3)+random.sample(mul8_name,3)+random.sample(add16_name,1)+random.sample(mul11_name,1)+random.sample(sub10_name,3)+random.sample(mul8_name,3)+random.sample(add16_name,1)+random.sample(mul11_name,1)
sample_all=10000
sample_num=1
pareto_front=[]
all_design_point=[]
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
    all_node_latency=[]
    with open(path,"r")as file:
        lines=file.readlines()
    for design in lines:
        all_design_feature=design.split()
        all_design_name.append(all_design_feature[:17])
        all_node_latency.append(float(all_design_feature[-1]))
    return all_design_name,all_node_latency
def single_design_totensor_hardware(single_design):
    all_design_input=[]
    mul11_dict=txt_to_dictkey("RF_data/kmeans_lib/pre_pruning_mul11.txt")
    mul8_dict=txt_to_dictkey("RF_data/kmeans_lib/pre_pruning_mul8.txt")
    add16_dict = txt_to_dictkey("RF_data/kmeans_lib/pre_pruning_add16.txt")
    sub10_dict=txt_to_dictkey("RF_data/kmeans_lib/pre_pruning_sub10.txt")
    for uint_design in single_design:
        if uint_design in sub10_dict:
            sub10_deisgn_in=eval(sub10_dict.get(uint_design))
            all_design_input.extend(list(sub10_deisgn_in[:3]))
        elif uint_design in mul8_dict:
            mul8_design_in = eval(mul8_dict.get(uint_design))
            all_design_input.extend(list(mul8_design_in[:3]))
        elif uint_design in add16_dict:
            add16_design_in=eval(add16_dict.get(uint_design))
            all_design_input.extend(list(add16_design_in[:3]))
        elif uint_design in mul11_dict:
            mul11_design_in = eval(mul11_dict.get(uint_design))
            all_design_input.extend(list(mul11_design_in[:3]))
        else:
            print(uint_design)
    return all_design_input
def single_design_totensor_ssim(single_design):
    all_design_input = []
    mul11_dict = txt_to_dictkey("RF_data/kmeans_lib/pre_pruning_mul11.txt")
    mul8_dict = txt_to_dictkey("RF_data/kmeans_lib/pre_pruning_mul8.txt")
    add16_dict = txt_to_dictkey("RF_data/kmeans_lib/pre_pruning_add16.txt")
    sub10_dict = txt_to_dictkey("RF_data/kmeans_lib/pre_pruning_sub10.txt")
    for uint_design in single_design:
        if uint_design in sub10_dict:
            sub10_deisgn_in = eval(sub10_dict.get(uint_design))
            all_design_input.extend([sub10_deisgn_in[-1]])
        elif uint_design in mul8_dict:
            mul8_design_in = eval(mul8_dict.get(uint_design))
            all_design_input.extend([mul8_design_in[-1]])
        elif uint_design in add16_dict:
            add16_design_in = eval(add16_dict.get(uint_design))
            all_design_input.extend([add16_design_in[-1]])
        elif uint_design in mul11_dict:
            mul11_design_in = eval(mul11_dict.get(uint_design))
            all_design_input.extend([mul11_design_in[-1]])
    return all_design_input
regressor_area=joblib.load("RF_data/kmeans_model/area_gaussion.m")
regressor_power=joblib.load("RF_data/kmeans_model/power_gaussion.m")
regressor_latency=joblib.load("RF_data/kmeans_model/latency_gaussion.m")
regressor_ssim=joblib.load("RF_data/kmeans_model/ssim_gaussion.m")
def random_forest(init_set):
    #print(init_set)
    hardware_in=single_design_totensor_hardware(init_set)
    wmed_in = single_design_totensor_ssim(init_set)
    area = regressor_area.predict([hardware_in])
    power = regressor_power.predict([hardware_in])
    latency = regressor_latency.predict([hardware_in])
    ssim = regressor_ssim.predict([wmed_in])
    return area[0],power[0],latency[0],ssim[0]
def getneighbour(start_set):
    neighbour=[]
    for idx in range(0,16):
        if idx<=2 or 8<=idx<=10:
            single_uint_lib=[single for single in sub10_name if single != start_set[idx]]
            for uint in single_uint_lib:
                ori_set =copy.deepcopy(start_set)
                ori_set[idx]=uint
                neighbour.append(ori_set)
        elif 3<=idx<=5 or 11<=idx<=13:
            single_uint_lib=[single for single in mul8_name if single != start_set[idx]]
            for uint in single_uint_lib:
                ori_set = copy.deepcopy(start_set)
                ori_set[idx]=uint
                neighbour.append(ori_set)
        elif idx==6 or idx==14:
            single_uint_lib=[single for single in add16_name if single != start_set[idx]]
            for uint in single_uint_lib:
                ori_set = copy.deepcopy(start_set)
                ori_set[idx]=uint
                neighbour.append(ori_set)
        elif idx==7 or idx==15:
            single_uint_lib=[single for single in mul11_name if single != start_set[idx]]
            for uint in single_uint_lib:
                ori_set = copy.deepcopy(start_set)
                ori_set[idx]=uint
                neighbour.append(ori_set)
    return neighbour
def new_pareto_front(pareto_front):
    area=np.empty((0,))
    ssim=np.empty((0,))
    del_lib=np.empty((0,))
    for single in pareto_front:
        area=np.append(area,single[0])
        ssim=np.append(ssim,single[3])
    #print(area,latency)
    for area1,ssim1 in zip(area,ssim):
        idx_area=np.where(area>area1)
        idx_ssim=np.where(ssim<ssim1)
        del_num=np.intersect1d(idx_area,idx_ssim)
        del_lib=np.union1d(del_num,del_lib)
    if len(del_lib) != 0:
        del_lib=np.around(del_lib).astype(int)
       # print(del_lib,type(del_lib))
        #print(pareto_front)
        new_pareto_front=[pareto_front[i] for i in range(len(pareto_front)) if i not in del_lib.tolist()]
        return new_pareto_front
    else:
        return pareto_front
area_init,power_init,latency_init,ssim_init=random_forest(init_set)
pareto_front.append([area_init,power_init,latency_init,ssim_init])
while sample_num!=sample_all:
    neighbour=getneighbour(init_set)
    next_design=random.choices(neighbour)
    area,power,latency,ssim=random_forest(next_design[0])
    all_design_point.append([area, power, latency, ssim])
    for pareto in pareto_front:
            if latency<pareto[2] or ssim>pareto[3]:
                pareto_front.append([area,power,latency,ssim])
                init_set=next_design[0]
                break;
    #print("pareto_front",pareto_front)
    pareto_front=new_pareto_front(pareto_front)
    #print("new_pareto_front",pareto_front)
    sample_num +=1
    print("len",len(pareto_front))
    print("sample",sample_num)
with open("pareto_对比/kmeans/mountain/all_design_latency_ssim_1w.txt", "w") as file:
    for item in all_design_point:
        design=str(item[0])+" "+str(item[1])+" "+str(item[2])+" "+str(item[3])
        file.write(design+"\n")