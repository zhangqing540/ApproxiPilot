import numpy as np
import matplotlib.pyplot as plt

# 读取第一个txt文件
target='test_dataset/gat/2w/latency_target.txt'
output='test_dataset/gat/2w/latency_output.txt'
with open(target, 'r') as file1:
    lines1 = file1.readlines()

# 读取第二个txt文件
with open(output, 'r') as file2:
    lines2 = file2.readlines()
'''
#area
target_value = np.array([float(line.strip())*1000+1500 for line in lines1])
output_value = np.array([float(line.strip())*1000+1500 for line in lines2])

#power
target_value = np.array([float(line.strip())+0.5 for line in lines1])
output_value = np.array([float(line.strip())+0.5 for line in lines2])

#latency
target_value = np.array([float(line.strip())+2.5 for line in lines1])
output_value = np.array([float(line.strip())+2.5 for line in lines2])
'''
#ssim
target_value = np.array([float(line.strip()) for line in lines1])
output_value = np.array([float(line.strip()) for line in lines2])

len=len(target_value)
print(len)
rate=[0,0,0,0,0]
for idx in range(len):
    abs_value=abs((target_value[idx]-output_value[idx])/output_value[idx])
    if abs_value<0.01:
        rate[0]=rate[0]+1
    elif 0.01<abs_value<0.02:
        rate[1]=rate[1]+1
    elif 0.02<abs_value<=0.03:
        rate[2]=rate[2]+1
    elif 0.03<abs_value<=0.04:
        rate[3]=rate[3]+1
    else:
        rate[4]=rate[4]+1
rate=np.array(rate)/2835
print(rate)




