import random
from gnn_model.test_sample_sobel import *
add8_lib={
        "add8u_1":[379.2,0.09,1.98,42.36,11,563,65,0],
        "add8u_0E2":[ 76.5,0.019 ,0.51 ,32.96 ,1.25 ,1488.5 ,85,0 ],
        "add8u_0NH": [429.1,0.1058,1.16 ,2 ,0.66 ,10 ,8 ,0],
        "add8u_0NQ": [369.23,0.078,0.76 ,7.87 ,0.66 ,190.5 ,44,0 ],
        "add8u_0NS": [375.88,0.08893,0.90 ,3.75 ,0.5 ,46 ,19,0],
        "add8u_0PA": [282.74,0.0625,0.76 ,8.023 ,4 ,123.5 ,32 ,0],
        "add8u_0TP": [176.29,0.0443,0.82 ,10.14 ,32 ,154 ,32,0 ],
        "add8u_2J3": [266.11,0.06640,1.02 ,12.5 ,3.125 ,186 ,25,0],
        "add8u_2LL": [229.52,0.06098,0.95 ,8.4375 ,1 ,99.5 ,22,0 ],
        "add8u_3RE": [146.36,0.03908,0.76 ,17.41 ,15 ,432 ,51,0 ],
        "add8u_05G": [409.14,0.1148,1.32 ,1.125 ,2 ,2 ,2 ,0],
        "add8u_6FT": [439.08,0.08823,1.32 ,4.625 ,9 ,32.5 ,15 ,0],
        "add8u_6K6": [399.17,0.0999,1.39 ,1.78 ,1 ,6.5 ,7 ,0],
        "add8u_6QU": [362.57,0.0841,1.47 ,3.95 ,6 ,27 ,15 ,0],
        "add8u_6R6": [242.82,0.06670,1.09 ,5.375 ,8 ,43.5 ,16 ,0],
        "add8u_108": [226.20,0.050672,0.76 ,8.4 ,8 ,123.25 ,31,0 ]
    }
add9_lib={
        "add9_2":[542.2,0.1505,1.99,4.75,1,37.5,10,0],
        "add9_7": [565.5,0.1625,1.79,1.25,3,2.5,3,0],
        "add9_9": [489,0.1283,2.2 ,5.421 ,1 ,43.5,15,0],
        "add9_10": [415,0.1094,1.76,12.625, 28, 234, 30,0],
        "add9_14": [492.3,0.1283, 2.26,10,24,156.6,24,0],
        "add9_15": [548.9,0.1532,2.66,10,24,156.5,24,0],
        "add9_16": [502.3,0.1241,2.08,10.44,20,164.5,29,0],
        "add9_18": [462.4,0.1138,2.30,10.65,30,170.5,31,0],
        "add9_21": [479,0.1259,2.15,25,1,946,50,0],
        "add9_23": [449,0.1107,1.95,18,42,558,47,0],
        "add9_27": [505.61,0.1276,2.02,9.29,5,111,21,0],
        "add9_28": [462.36,0.1171,2.39,10.78,30,174.5,31,0],
        "add9_30": [465.59,0.1130,2,18.91,8,568,46,0],
        "add9_31": [439.08,0.1090,2.14,10.658,6,170,29,0],
        "add9_33": [552.18,0.1434,2.05,17.78,16,440.5,40,0],
        "add9_35": [515.59,0.1438,2.10,2.875,1,12.5,7,0]
    }
sub10_lib={
        "sub10_1":[695.5,0.2063,2.30,0.5,1,0.5,1,1],
        "sub10_2": [681.91,0.1963,2.43,8.5,2,129.87,18,1],
        "sub10_3": [665.2,0.1844,2.53,2.25,5,8.991,5 ,1],
        "sub10_4": [608.73,0.1720,2.48 ,2.75,7,10.5,7 ,1],
        "sub10_5": [628.68,0.1730,2.43,2.5,6 ,9.996 ,6 ,1],
        "sub10_6": [605.40,0.1732,2 ,3.5,7,11.5 ,7 ,1],
        "sub10_7": [568.81,0.1563,2.60 ,7.5 ,15 ,42.48 ,15 ,1],
        "sub10_8": [538.87,0.1358,2.68 ,9.31 ,22 ,168.34 ,31 ,1],
        "sub10_9": [515.59,0.1306, 2.50, 4.43, 23,133.28 ,25 ,1]
    }
add8_name=["add8u_1","add8u_0E2","add8u_0NH","add8u_0NQ","add8u_0NS","add8u_0PA","add8u_0TP","add8u_2J3","add8u_2LL","add8u_3RE","add8u_05G","add8u_6FT","add8u_6K6","add8u_6QU","add8u_6R6","add8u_108"]
add9_name=["add9_2","add9_7","add9_9","add9_10","add9_14","add9_15","add9_16","add9_18","add9_21","add9_23","add9_27","add9_28","add9_30","add9_31","add9_33","add9_35"]
sub10_name=["sub10_2","sub10_1","sub10_3","sub10_4","sub10_5","sub10_6","sub10_7","sub10_8","sub10_9"]
init_set=["add8u_0NH","add8u_0NH","add9_7","add9_7","sub10_1"]
def getneighbour(start_set):
    neighbour=[]
    pruning_add81=[single for single in add8_name if single != start_set[0]]
    pruning_add82=[single for single in add8_name if single != start_set[1]]
    pruning_add91=[single for single in add9_name if single != start_set[2]]
    pruning_add92=[single for single in add9_name if single != start_set[3]]
    pruning_sub10= [single for single in sub10_name if single != start_set[4]]
    [neighbour.append([add81,start_set[1],start_set[2],start_set[3],start_set[4]]) for add81 in pruning_add81]
    [neighbour.append([start_set[0],add82,start_set[2],start_set[3],start_set[4]]) for add82 in pruning_add82]
    [neighbour.append([start_set[0],start_set[1],add91,start_set[3],start_set[4]]) for add91 in pruning_add91]
    [neighbour.append([start_set[0],start_set[1],start_set[2],add92,start_set[4]]) for add92 in pruning_add92]
    [neighbour.append([start_set[0],start_set[1],start_set[2],start_set[3],sub10]) for sub10 in pruning_sub10]
    return neighbour
def new_pareto_front(pareto_front):
    area=np.empty((0,))
    power = np.empty((0,))
    latency = np.empty((0,))
    ssim=np.empty((0,))
    del_lib=np.empty((0,))
    for single in pareto_front:
        area=np.append(area,single[0])
        ssim=np.append(ssim,single[3])
    #print(area,latency)
    for area1,ssim1 in zip(area,ssim):
        idx_latency=np.where(area>area1)
        idx_ssim=np.where(ssim<ssim1)
        del_num=np.intersect1d(idx_latency,idx_ssim)
        del_lib=np.union1d(del_num,del_lib)
    if len(del_lib) != 0:
        del_lib=np.around(del_lib).astype(int)
       # print(del_lib,type(del_lib))
        #print(pareto_front)
        new_pareto_front=[pareto_front[i] for i in range(len(pareto_front)) if i not in del_lib.tolist()]
        return new_pareto_front
    else:
        return pareto_front
sample_all=5000
sample_num=1
pareto_front=[]
area_init,power_init,latency_init,ssim_init=sample_test(add81=init_set[0],add82=init_set[1],add91=init_set[2],add92=init_set[3],sub10=init_set[4])
pareto_front.append([area_init,power_init,latency_init,ssim_init])
while sample_num!=sample_all:
    neighbour=getneighbour(init_set)
    next_design=random.choices(neighbour)
    area,power,latency,ssim=sample_test(add81=next_design[0][0],add82=next_design[0][1],add91=next_design[0][2],add92=next_design[0][3],sub10=next_design[0][4])
    if ssim < 1:
        for pareto in pareto_front:
            # print(area,pareto_对比[0])
            # exit(0)
            if area < pareto[0] or ssim > pareto[3]:
                pareto_front.append([area, power, latency, ssim])
                init_set = next_design[0]
                break;
    #print(len(pareto_front))
    pareto_front=new_pareto_front(pareto_front)
    sample_num +=1
    print("len",len(pareto_front))
    print("sample",sample_num)
with open("different_sample_function/pashan/pashan_area_ssim_good.txt", "w") as file:
    for item in pareto_front:
        design=str(item[0])+" "+str(item[1])+" "+str(item[2])+" "+str(item[3])
        file.write(design+"\n")