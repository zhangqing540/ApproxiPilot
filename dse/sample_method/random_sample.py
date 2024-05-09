import random
from gnn_model.test_sample_sobel import *
random_sample_dataset="sample_dataset/gaussion/random_sample4.txt"
random_num=10000
add8_lib = ["add8u_1","add8u_0E2","add8u_0NH","add8u_0NQ","add8u_0NS","add8u_0PA","add8u_0TP","add8u_2J3","add8u_2LL","add8u_3RE","add8u_05G","add8u_6FT","add8u_6K6","add8u_6QU","add8u_6R6","add8u_108"]
add9_lib = ["add9_2","add9_7","add9_9","add9_10","add9_14","add9_15","add9_16","add9_18","add9_21","add9_23","add9_27","add9_28","add9_30","add9_31","add9_33","add9_35"]
sub10_lib = ["sub10_1","sub10_2","sub10_3","sub10_4","sub10_5","sub10_6","sub10_7","sub10_8","sub10_9"]
all_design_lib = []
for sub10_single in sub10_lib:
    for add92_single in add9_lib:
        for add91_single in add9_lib:
            for add82_single in add8_lib:
                for add81_single in add8_lib:
                    single_design_lib = add81_single + " " + add82_single + " " + add91_single + " " + add92_single + " " + sub10_single
                    all_design_lib.append(single_design_lib)
random_sample=random.sample(all_design_lib,random_num)
with open(random_sample_dataset,"a") as file:
    for single in random_sample:
        add81,add82,add91,add92,sub10=single.split(" ")
        area,power,latency,ssim=sample_test(add81,add82,add91,add92,sub10)
        result=str(area)+" "+str(power)+" "+str(latency)+" "+str(ssim)
        file.write(result+"\n")
