import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image
def paixu(Area, Ssim):
    combined = list(zip(Area, Ssim))
    sorted_combined = sorted(combined, key=lambda x: x[0], reverse=True)
    sorted_area, sorted_ssim = zip(*sorted_combined)
    return sorted_area, sorted_ssim
def read_file(file_path):
    data_ours = pd.read_csv(file_path, sep=" ", header=None, names=["area", "power", "latency", "ssim"])
    # 将数据存储到四个变量中
    area = data_ours["area"]
    latency = data_ours["latency"]
    power = data_ours["power"]
    ssim = data_ours["ssim"]
    return area,power,latency,ssim


def pareto_front(area_ours, ssim_ours):
    del_lib = np.empty((0,))
    for area1, ssim1 in zip(area_ours, ssim_ours):
        idx_area = np.where(area_ours > area1)
        idx_ssim = np.where(ssim_ours < ssim1)
        del_num = np.intersect1d(idx_area, idx_ssim)
        del_lib = np.union1d(del_num, del_lib)

    if len(del_lib) != 0:
        del_lib = np.around(del_lib).astype(int)
        new_area = [area_ours[i] for i in range(len(area_ours)) if i not in del_lib.tolist()]
        new_ssim = [ssim_ours[i] for i in range(len(ssim_ours)) if i not in del_lib.tolist()]
    else:
        new_area,new_ssim=[],[]
    ddl_area,ddl_ssim=paixu(new_area,new_ssim)
    return ddl_area,ddl_ssim
bayssion_area_ssim="pareto_对比/diff_sample/bayssion_area_ssim.txt"
nsga2_area_ssim="pareto_对比/diff_sample/nsga2_area_ssim.txt"
nsga3_area_ssim="pareto_对比/diff_sample/nsga3_area_ssim.txt"
random_area_ssim="pareto_对比/diff_sample/random_area_ssim.txt"
area_bay,power_bay,latency_bay,ssim_bay=read_file(bayssion_area_ssim)
area_nsga2,power_nsga2,latency_nsga2,ssim_nsga2=read_file(nsga2_area_ssim)
area_nsga3,power_nsga3,latency_nsga3,ssim_nsga3=read_file(nsga3_area_ssim)
area_random,power_random,latency_random,ssim_random=read_file(random_area_ssim)
pareto_bay_area,pareto_bay_ssim=pareto_front(area_bay,ssim_bay)
pareto_nsga2_area,pareto_nsga2_ssim=pareto_front(area_nsga2,ssim_nsga2)
pareto_nsga3_area,pareto_nsga3_ssim=pareto_front(area_nsga3,ssim_nsga3)
pareto_random_area,pareto_random_ssim=pareto_front(area_random,ssim_random)
plt.figure()
#plt.scatter(area_ours,ssim_ours,label='ApproxPilot', color='darkorange', marker='o',s=2)
#plt.scatter(area_auto_all, ssim_auto_all,label='Autoax', color='dodgerblue', marker='o',s=2)
#area_pareto_ours,ssim_pareto_ours=paixu(new_area,new_ssim)
#area_pareto_auto,ssim_pareto_auto=paixu(area_auto,ssim_auto)
#print(area_pareto_ours)
plt.plot(pareto_bay_ssim,pareto_bay_area, marker='o', linestyle='-', color='b', label='TPE_bayesian',markersize=2)
plt.plot(pareto_nsga2_ssim,pareto_nsga2_area, marker='o', linestyle='-', color='g', label='nsga2',markersize=2)
plt.plot(pareto_nsga3_ssim,pareto_nsga3_area, marker='o', linestyle='-', color='r', label='nsga3',markersize=2)
plt.plot(pareto_random_ssim,pareto_random_area, marker='o', linestyle='-', color='k', label='random',markersize=2)
plt.legend(loc='best', fontsize=10, markerscale=2,frameon=False)
plt.ylabel('Area($um^2$)')
plt.xlabel('Ssim')
plt.gca().invert_xaxis()
plt.savefig("pic/different_sample_model.pdf", format="pdf")
# 显示图形
plt.show()
print("bay",len(list(set(pareto_bay_area))))
print("nsga2",len(list(set(pareto_nsga2_area))))
print("nsga3",len(list(set(pareto_nsga3_area))))
print("random",len(list(set(pareto_random_area))))
#plt.savefig("pic/different_sample_model.pdf", format="pdf")
#pareto_front_num=list(area_pareto_ours)
#print(len(list(set(pareto_front_num))))
#num_bay=list(set(pareto_nsga2_area)
#num_random=
#num_nsga2=
#num_nsga3=


