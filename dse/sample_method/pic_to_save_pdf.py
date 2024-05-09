import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image
ours_file= "pareto_对比/sobel/贝叶斯/bayssion_area_ssim11.txt"
# 读取文本文件并提取数据
data_ours = pd.read_csv(ours_file, sep=" ", header=None, names=["area", "power", "latency", "ssim"])
# 将数据存储到四个变量中
area_ours = data_ours["area"]
latency_ours=data_ours["latency"]
#power_ours=data_ours["power"]
ssim_ours = data_ours["ssim"]
del_lib=np.empty((0,))
for area1, ssim1 in zip(area_ours, ssim_ours):
    idx_area = np.where(area_ours > area1)
    idx_ssim = np.where(ssim_ours< ssim1)
    del_num = np.intersect1d(idx_area, idx_ssim)
    del_lib = np.union1d(del_num, del_lib)

if len(del_lib) != 0:
    del_lib = np.around(del_lib).astype(int)
    # print(del_lib,type(del_lib))
    # print(pareto_front)
    new_area = [area_ours[i] for i in range(len(area_ours)) if i not in del_lib.tolist()]
    new_ssim = [ssim_ours[i] for i in range(len(ssim_ours)) if i not in del_lib.tolist()]
auto="paerto_对比/sobel"
# 读取文本文件并提取数据
data_auto = pd.read_csv(auto, sep=" ", header=None, names=["area", "power", "latency", "ssim"])

# 将数据存储到四个变量中
area_auto = data_auto["area"]
power_auto = data_auto["power"]
latency_auto = data_auto["latency"]
ssim_auto = data_auto["ssim"]

plt.figure()
plt.scatter(new_area,new_ssim,label='ApproxPilot', color='red', marker='o',)
plt.scatter(area_auto, ssim_auto,label='autoAx', color='blue', marker='o')
plt.legend(loc='best', fontsize=10, markerscale=1,frameon=False)
plt.xlabel('Area')
plt.ylabel('Ssim')

plt.savefig("pic/compare_autoax.pdf", format="pdf")
# 显示图形
plt.show()



