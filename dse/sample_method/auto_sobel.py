import random
from gnn_model.test_sample_sobel import *
import pandas as pd
import numpy as np
import torch
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import ast
import joblib

def read_file(file_name):
    data = []
    node_name=[]
    with open(file_name, 'r') as file:
        for line in file:
            numbers = line.strip().split(" ")
            name=numbers[0]+" "+numbers[1]+" "+numbers[2]+" "+numbers[3]+" "+numbers[4]
            area=numbers[5]
            power=numbers[6]
            latency=numbers[7]
            ssim=numbers[8]
            #link=ast.literal_eval(numbers[-1])
            #one_data = [float(latency)]
            one_data=[float(area),float(power),float(latency),float(ssim)]
            #print("one", one_data)
            data.append(one_data)
            #print("data",data)
            node_name.append(name)
            #link_lib.append(link)
            #print(link)
    return node_name,data
def node_feature(input_feature):
    #8--200 9-250  10-300
    add8_uint_lib={}
    add12_uint_lib={}
    sub10_uint_lib={}
    add8_pruning_path = "RF_data/lib/pre_pruning_add8.txt"
    add12_pruning_path = "RF_data/lib/pre_pruning_add12.txt"
    sub10_pruning_path = "RF_data/lib/pre_pruning_sub10.txt"
    with open(add8_pruning_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            key, value = line.strip().split(': ')
            add8_uint_lib[key] = value
    with open(add12_pruning_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            key, value = line.strip().split(': ')
            add12_uint_lib[key] = value
    with open(sub10_pruning_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            key, value = line.strip().split(': ')
            sub10_uint_lib[key] = value
    add81,add82,add91,add92,sub101=input_feature.split()
    #print(add81,add82,add91,add92,sub101)
    #print("input",feature81,feature82,feature91,feature92,feature10)
    feature81=ast.literal_eval(add8_uint_lib.get(add81))
    feature82=ast.literal_eval(add8_uint_lib.get(add82))
    feature91=ast.literal_eval(add12_uint_lib.get(add91))
    feature92=ast.literal_eval(add12_uint_lib.get(add92))
    feature10=ast.literal_eval(sub10_uint_lib.get(sub101))

    #exit(0)
    all_feature_hardware=feature81[0:3]+feature82[0:3]+feature91[0:3]+feature92[0:3]+feature10[0:3]
    #all_feature_wmed = feature81[0:3] + feature82[0:3] + feature91[0:3] + feature92[0:3] + feature10[0:3]
    all_feature_wmed=[feature81[3],feature82[3],feature91[3],feature92[3],feature10[3]]

    #all_feature = [0, 0, 0, 0, 0, 0, 0, 0]
    #for i in range(8):
     #   all_feature[i] = feature81[i]+feature82[i]+feature91[i]+feature92[i]+feature10[i]
    return all_feature_hardware,all_feature_wmed
'''
# 导入数据，路径中要么用\\或/或者在路径前加r
input_hardware=[]
input_wmed=[]
output_area=[]
output_power=[]
output_latency=[]
output_ssim=[]
dataset_file= "RF_data/sobel/dataset/autoax_sobel_4w.txt"
node_name,label_list=read_file(dataset_file)
all_dataset=zip(node_name,label_list)
for node_name_single,label_single in all_dataset:
    #print(node_name_single)
    hardware_in, wmed_in=node_feature(node_name_single)
    input_hardware.append(hardware_in)
    input_wmed.append(wmed_in)
    output_area.append(label_single[0])
    output_power.append(label_single[1])
    output_latency.append(label_single[2])
    output_ssim.append(label_single[3])
# 将数据分为训练集和测试集
area_train_data, area_test_data, area_train_label, area_test_label = train_test_split(input_hardware,
                                                    output_area,
                                                    test_size=0.01,
                                                    random_state=0,
                                                    shuffle=True)

power_train_data, power_test_data, power_train_label, power_test_label = train_test_split(input_hardware,
                                                    output_power,
                                                    test_size=0.01,
                                                    random_state=0,
                                                    shuffle=True)
latency_train_data, latency_test_data, latency_train_label, latency_test_label = train_test_split(input_hardware,
                                                    output_latency,
                                                    test_size=0.01,
                                                    random_state=0,
                                                    shuffle=True)
ssim_train_data, ssim_test_data, ssim_train_label, ssim_test_label = train_test_split(input_wmed,
                                                    output_ssim,
                                                    test_size=0.01,
                                                    random_state=0,
                                                    shuffle=True)
# 训练随机森林解决回归问题
from sklearn.ensemble import RandomForestRegressor
regressor_area= RandomForestRegressor(n_estimators=100, random_state=0)
regressor_area.fit(area_train_data, area_train_label)
joblib.dump(regressor_area,"RF_data/model/area_sobel.m")
regressor_power= RandomForestRegressor(n_estimators=100, random_state=0)
regressor_power.fit(power_train_data, power_train_label)
joblib.dump(regressor_power,"RF_data/model/power_sobel.m")
regressor_latency= RandomForestRegressor(n_estimators=100, random_state=0)
regressor_latency.fit(latency_train_data, latency_train_label)
joblib.dump(regressor_latency,"RF_data/model/latency_sobel.m")
regressor_ssim= RandomForestRegressor(n_estimators=100, random_state=0)
regressor_ssim.fit(ssim_train_data, ssim_train_label)
joblib.dump(regressor_ssim,"RF_data/model/ssim_sobel.m")
'''
regressor_area=joblib.load("RF_data/model/area_sobel.m")
regressor_power=joblib.load("RF_data/model/power_sobel.m")
regressor_latency=joblib.load("RF_data/model/latency_sobel.m")
regressor_ssim=joblib.load("RF_data/model/ssim_sobel.m")
add8_name=["add8u_6SM","add8u_0E2","add8u_6K6","add8u_108","add8u_6LG","add8u_6TH","add8u_2AM","add8u_6S4","add8u_0NS","add8u_6MZ","add8u_6PT","add8u_6P8","add8u_2LL","add8u_0PA","add8u_6R6","add8u_0TP","add8u_05G","add8u_02Y","add8u_1HG","add8u_6QU","add8u_6FT","add8u_00M","add8u_0D0","add8u_0UK","add8u_0NQ","add8u_0JM","add8u_0PL","add8u_3RE"]
add12_name=["add12u_3UT","add12u_2KC","add12u_0Z5","add12u_0G8","add12u_0B6","add12u_50U","add12u_22J","add12u_06R","add12u_2L1","add12u_0JK","add12u_3K3","add12u_39N","add12u_2UH","add12u_2UF","add12u_38J","add12u_0ZP","add12u_0AZ","add12u_0PX","add12u_4NT","add12u_3L3","add12u_0C9","add12u_0UZ","add12u_4TF","add12u_28B","add12u_0LN"]
sub10_name=["sub10_90","sub10_260","sub10_1","sub10_130","sub10_270","sub10_15","sub10_135","sub10_5","sub10_210","sub10_26","sub10_6","sub10_85","sub10_200"]
init_set=random.choice(add8_name)+" "+random.choice(add8_name)+" "+random.choice(add12_name)+" "+random.choice(add12_name)+" "+random.choice(sub10_name)
def random_forest(init_set):
    print(init_set)
    hardware_in, wmed_in=node_feature(init_set)
    area = regressor_area.predict([hardware_in])
    power = regressor_power.predict([hardware_in])
    latency = regressor_latency.predict([hardware_in])
    ssim = regressor_ssim.predict([wmed_in])
    #print("model_out",area,power,latency,ssim)
    return area[0],power[0],latency[0],ssim[0]
def getneighbour(start_set1):
    add81, add82, add91, add92, sub101 = start_set1.split()
    start_set=[add81,add82,add91,add92,sub101]
    neighbour=[]
    pruning_add81=[single for single in add8_name if single != start_set[0]]
    pruning_add82=[single for single in add8_name if single != start_set[1]]
    pruning_add121=[single for single in add12_name if single != start_set[2]]
    pruning_add122=[single for single in add12_name if single != start_set[3]]
    pruning_sub10= [single for single in sub10_name if single != start_set[4]]

    [neighbour.append([add81,start_set[1],start_set[2],start_set[3],start_set[4]]) for add81 in pruning_add81]
    [neighbour.append([start_set[0],add82,start_set[2],start_set[3],start_set[4]]) for add82 in pruning_add82]
    [neighbour.append([start_set[0],start_set[1],add121,start_set[3],start_set[4]]) for add121 in pruning_add121]
    [neighbour.append([start_set[0],start_set[1],start_set[2],add122,start_set[4]]) for add122 in pruning_add122]
    [neighbour.append([start_set[0],start_set[1],start_set[2],start_set[3],sub10]) for sub10 in pruning_sub10]
    next_choice_list=random.choice(neighbour)
    next_choice=next_choice_list[0]+" "+next_choice_list[1]+" "+next_choice_list[2]+" "+next_choice_list[3]+" "+next_choice_list[4]
    return next_choice
def new_pareto_front(pareto_front):
    area=np.empty((0,))
    ssim=np.empty((0,))
    del_lib=np.empty((0,))
    for single in pareto_front:
        area=np.append(area,single[2])
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
sample_all=20000
sample_num=1
pareto_front=[]
all_design_point=[]
#area_init,power_init,latency_init,ssim_init=sample_test(add81=init_set[0],add82=init_set[1],add91=init_set[2],add92=init_set[3],sub10=init_set[4])
area_init,power_init,latency_init,ssim_init=random_forest(init_set)
pareto_front.append([area_init,power_init,latency_init,ssim_init])
while sample_num!=sample_all:
    next_design=getneighbour(init_set)
    area,power,latency,ssim=random_forest(next_design)
    all_design_point.append([area, power, latency, ssim])
    for pareto in pareto_front:
            if power<pareto[1] or ssim>pareto[3]:
                pareto_front.append([area,power,latency,ssim])
                init_set=next_design
                break;
    #print("pareto_front",pareto_front)
    pareto_front=new_pareto_front(pareto_front)
    #print("new_pareto_front",pareto_front)
    sample_num +=1
    print("len",len(pareto_front))
    print("sample",sample_num)

#with open("pareto_对比/sobel/mountain/mountain_latency_ssim_5k.txt", "w") as file:
#    for item in pareto_front:
#        design=str(item[0])+" "+str(item[1])+" "+str(item[2])+" "+str(item[3])
#        file.write(design+"\n")

with open("pareto_对比/sobel/mountain/all_design_power_ssim_2w.txt", "w") as file:
    for item in all_design_point:
        design=str(item[0])+" "+str(item[1])+" "+str(item[2])+" "+str(item[3])
        file.write(design+"\n")