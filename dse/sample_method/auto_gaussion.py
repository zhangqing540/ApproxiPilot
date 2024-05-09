import random
#from gnn_model.test_sample_sobel import *
import pandas as pd
import numpy as np
import torch
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
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
mul_name=["mul8u_17R6", "mul8u_17C8", "mul8u_R36", "mul8u_T83","mul8u_874","mul8u_197B", "mul8u_2NDH", "mul8u_Z9D", "mul8u_L93","mul8u_17MJ", "mul8u_4X5", "mul8u_12KA", "mul8u_18UH","mul8u_19XF", "mul8u_ZDF", "mul8u_GTR", "mul8u_1JJQ","mul8u_1A0M", "mul8u_8U3", "mul8u_ZB3"]
add16_name=["add16u_0U8", "add16u_0KU", "add16u_0GX", "add16u_0PT", "add16u_0K3","add16u_0HK", "add16u_0EZ", "add16u_08V", "add16u_1A5", "add16u_126","add16u_0SL", "add16u_0J3", "add16u_162", "add16u_110", "add16u_15Q","add16u_067", "add16u_0SD", "add16u_0KG", "add16u_0RJ", "add16u_0NL"]
init_set=random.sample(mul_name,9)+random.sample(add16_name,8)
sample_all=50000
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
    mul8_dict=txt_to_dictkey("RF_data/lib/mul8.txt")
    add16_dict = txt_to_dictkey("RF_data/lib/add16.txt")
    for uint_design in single_design:
        if uint_design in mul8_dict:
            mul_deisgn_in=eval(mul8_dict.get(uint_design))
            all_design_input.extend(list(mul_deisgn_in[:3]))
        elif uint_design in add16_dict:
            add_design_in=eval(add16_dict.get(uint_design))
            all_design_input.extend(list(add_design_in[:3]))
    return all_design_input
def single_design_totensor_ssim(single_design):
    all_design_input=[]
    mul8_dict=txt_to_dictkey("RF_data/lib/mul8.txt")
    add16_dict = txt_to_dictkey("RF_data/lib/add16.txt")
    for uint_design in single_design:
        if uint_design in mul8_dict:
            mul_deisgn_in=eval(mul8_dict.get(uint_design))
            all_design_input.extend([mul_deisgn_in[-1]])
        elif uint_design in add16_dict:
            add_design_in=eval(add16_dict.get(uint_design))
            all_design_input.extend([add_design_in[-1]])
    return all_design_input
'''
# 导入数据，路径中要么用\\或/或者在路径前加r
all_designs_ssim,label_ssim=design_name_and_value(dataset_ssim)
for node_name_single,single_label_ssim in zip(all_designs_ssim,label_ssim):
    all_input=single_design_totensor_ssim(node_name_single)
    input_ssim.append(all_input)
    output_ssim.append(single_label_ssim)
print("ssim data end")
all_designs_area,label_area=design_name_and_value(dataset_area)
for node_name_single,single_label_area in zip(all_designs_area,label_area):
    all_input=single_design_totensor_hardware(node_name_single)
    input_area.append(all_input)
    output_area.append(single_label_area)
print("area data end")
all_designs_power,label_power=design_name_and_value(dataset_power)
for node_name_single,single_label_power in zip(all_designs_power,label_power):
    all_input=single_design_totensor_hardware(node_name_single)
    input_power.append(all_input)
    output_power.append(single_label_power)
print("power data end")
all_designs_latency,label_latency=design_name_and_value(dataset_latency)
for node_name_single,single_label_latency in zip(all_designs_latency,label_latency):
    all_input=single_design_totensor_hardware(node_name_single)
    input_latency.append(all_input)
    output_latency.append(single_label_latency)
print("latency data end")

# 将数据分为训练集和测试集
area_train_data, area_test_data, area_train_label, area_test_label = train_test_split(input_area,output_area,test_size=0.03,random_state=0,shuffle=True)
power_train_data, power_test_data, power_train_label, power_test_label = train_test_split(input_power,output_power,test_size=0.03,random_state=0,shuffle=True)
latency_train_data, latency_test_data, latency_train_label, latency_test_label = train_test_split(input_latency,output_latency,test_size=0.03,random_state=0,shuffle=True)
ssim_train_data, ssim_test_data, ssim_train_label, ssim_test_label = train_test_split(input_ssim,output_ssim,test_size=0.03,random_state=0,shuffle=True)
print("dataset split end")
# 训练随机森林解决回归问题
regressor_area= RandomForestRegressor(n_estimators=100, random_state=0)
regressor_area.fit(area_train_data, area_train_label)
joblib.dump(regressor_area,"RF_data/model/area_gaussion.m")
print("train area model end")
regressor_power= RandomForestRegressor(n_estimators=100, random_state=0)
regressor_power.fit(power_train_data, power_train_label)
joblib.dump(regressor_power,"RF_data/model/power_gaussion.m")
print("train power model end")
regressor_latency= RandomForestRegressor(n_estimators=100, random_state=0)
regressor_latency.fit(latency_train_data, latency_train_label)
joblib.dump(regressor_latency,"RF_data/model/latency_gaussion.m")
print("train latency model end")
regressor_ssim= RandomForestRegressor(n_estimators=100, random_state=0)
regressor_ssim.fit(ssim_train_data, ssim_train_label)
joblib.dump(regressor_ssim,"RF_data/model/ssim_gaussion.m")
print("train ssim model end")
'''
regressor_area=joblib.load("RF_data/model/area_gaussion.m")
regressor_power=joblib.load("RF_data/model/power_gaussion.m")
regressor_latency=joblib.load("RF_data/model/latency_gaussion.m")
regressor_ssim=joblib.load("RF_data/model/ssim_gaussion.m")
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
        if idx<=8:
            single_uint_lib=[single for single in mul_name if single != start_set[idx]]
            for uint in single_uint_lib:
                ori_set =copy.deepcopy(start_set)
                ori_set[idx]=uint
                neighbour.append(ori_set)
        elif idx<=9:
            single_uint_lib=[single for single in add16_name if single != start_set[idx]]
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
        area=np.append(area,single[1])
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
#area_init,power_init,latency_init,ssim_init=sample_test(add81=init_set[0],add82=init_set[1],add91=init_set[2],add92=init_set[3],sub10=init_set[4])
area_init,power_init,latency_init,ssim_init=random_forest(init_set)
#print(area_init,power_init,latency_init,ssim_init)
pareto_front.append([area_init,power_init,latency_init,ssim_init])
print(init_set)
while sample_num!=sample_all:
    neighbour=getneighbour(init_set)
    next_design=random.choices(neighbour)
    print(next_design[0])
    area,power,latency,ssim=random_forest(next_design[0])
    all_design_point.append([area, power, latency, ssim])
    for pareto in pareto_front:
            if power<pareto[1] or ssim>pareto[3]:
                pareto_front.append([area,power,latency,ssim])
                init_set=next_design[0]
                break;
    #print("pareto_front",pareto_front)
    pareto_front=new_pareto_front(pareto_front)
    #print("new_pareto_front",pareto_front)
    sample_num +=1
    #print("len",len(pareto_front))
    print("sample",sample_num)
with open("pareto_对比/gaussion/mountain/all_design_power_ssim_5w.txt", "w") as file:
    for item in all_design_point:
        design=str(item[0])+" "+str(item[1])+" "+str(item[2])+" "+str(item[3])
        file.write(design+"\n")