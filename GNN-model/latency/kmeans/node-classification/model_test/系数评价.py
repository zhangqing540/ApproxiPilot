from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# 读取第一个txt文件
area1="sobel/gsae/area_output.txt"
area2="sobel/gsae/area_target.txt"
power1="sobel/gsae/power_output.txt"
power2="sobel/gsae/power_target.txt"
latency1="sobel/gsae/latency_output.txt"
latency2="sobel/gsae/latency_target.txt"
ssim1="sobel/gsae/ssim_output.txt"
ssim2="sobel/gsae/ssim_target.txt"
with open(area1, 'r') as file1:
    area1 = file1.readlines()
# 读取第二个txt文件
with open(area2, 'r') as file2:
    area2 = file2.readlines()
with open(power1, 'r') as file1:
    power1 = file1.readlines()
# 读取第二个txt文件
with open(power2, 'r') as file2:
    power2 = file2.readlines()
with open(latency1, 'r') as file1:
    latency1= file1.readlines()
# 读取第二个txt文件
with open(latency2, 'r') as file2:
    latency2 = file2.readlines()
with open(ssim1, 'r') as file1:
    ssim1 = file1.readlines()
# 读取第二个txt文件
with open(ssim2, 'r') as file2:
    ssim2 = file2.readlines()

# 转换为浮点数
#area
area1 = np.array([((float(line.strip()))-1500)/1000 for line in area1])
area2 = np.array([((float(line.strip()))-1500)/1000 for line in area2])
power1 = np.array([(float(line.strip()))-0.5 for line in power1])
power2 = np.array([(float(line.strip()))-0.5 for line in power2])
latency1 = np.array([(float(line.strip()))-2.5 for line in latency1])
latency2 = np.array([(float(line.strip()))-2.5 for line in latency2])
ssim1 = np.array([(float(line.strip())) for line in ssim1])
ssim2 = np.array([(float(line.strip())) for line in ssim2])
'''
mse_area=mean_squared_error(area1, area2)
mse_power=mean_squared_error(power1,power2)
mse_latency=mean_squared_error(latency1,latency2)
mse_ssim=mean_squared_error(ssim1,ssim2)
ave_mse=(mse_area+mse_power+mse_latency+mse_ssim)/4
mae_area=mean_absolute_error(area1, area2)
mae_power=mean_absolute_error(power1,power2)
mae_latency=mean_absolute_error(latency1,latency2)
mae_ssim=mean_absolute_error(ssim1,ssim2)
ave_mae=(mae_area+mae_power+mae_latency+mae_ssim)/4
'''
r2_area=r2_score(area1, area2)
r2_power=r2_score(power1,power2)
r2_latency=r2_score(latency1,latency2)
r2_ssim=r2_score(ssim1,ssim2)
print("area",r2_area)
print("power",r2_power)
print("latency",r2_latency)
print("ssim",r2_ssim)

