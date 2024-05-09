from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.metrics import mean_squared_error,mean_absolute_percentage_error
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# 读取第一个txt文件

latency1="../result/label.txt"
latency2="../result/pred.txt"
with open(latency1, 'r') as file1:
    latency_label= file1.readlines()
# 读取第二个txt文件
with open(latency2, 'r') as file2:
    latency_pred = file2.readlines()
latency1 = np.array([(float(line.strip())) for line in latency_label])
latency2 = np.array([(float(line.strip()))*2000 for line in latency_pred])
r2_latency=r2_score(latency1,latency2)
mape=mean_absolute_percentage_error(latency1,latency2)
print("latency",r2_latency)
print("latency",mape)


