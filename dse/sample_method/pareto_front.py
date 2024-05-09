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
def read_file(file_path,ssim_limit=0):
    data_ours = pd.read_csv(file_path, sep=" ", header=None, names=["area", "power", "latency", "ssim"])
    data_ours.drop_duplicates(inplace=True)
    area = np.array(data_ours["area"])
    latency = np.array(data_ours["latency"])
    power = np.array(data_ours["power"])
    ssim = np.array(data_ours["ssim"])
    indices=np.where((ssim>=0))

    final_area=area[indices]
    final_power=power[indices]
    final_latency=latency[indices]
    final_ssim=ssim[indices]
    return final_area,final_power,final_latency,final_ssim
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
ours_file= "pareto_对比/gaussion/bayession/bayession_area_ssim.txt"
autoAx_all="pareto_对比/gaussion/mountain/all_design_area_ssim.txt"
#ours_file= "pareto_对比/gaussion/bayession/bayession_latency_ssim_5w.txt"
#autoAx_all="pareto_对比/gaussion/mountain/all_design_latency_ssim_3w.txt"
# 读取文本文件并提取数据
area_our,power_our,latency_our,ssim_our=read_file(ours_file)
area_auto,power_auto,latency_auto,ssim_auto=read_file(autoAx_all)
pareto_our_area,pareto_our_ssim=pareto_front(area_our,ssim_our)
pareto_auto_area,pareto_auto_ssim=pareto_front(area_auto,ssim_auto)
print(len(list(pareto_our_area)))
#print(len(list(pareto_auto_area)))
for area,ssim in zip(pareto_our_area,pareto_our_ssim):
    print(area,ssim)
plt.figure()
plt.scatter(ssim_our,area_our, color='silver', marker='o',s=5)
plt.scatter(ssim_auto,area_auto, color='silver', marker='o',s=5)
plt.plot(pareto_auto_ssim,(pareto_auto_area), color='#848484', marker='s',markersize=4)
plt.plot(pareto_our_ssim,(pareto_our_area),color='#4f4f4f', marker='o',markersize=4)
plt.legend(" ", fontsize=10, markerscale=2,frameon=False)
#plt.xlabel('latency')
plt.gca().invert_xaxis()
plt.yticks(fontproperties='Times New Roman', size=25,weight='bold')#设置大小及加粗
plt.xticks(fontproperties='Times New Roman', size=25)
plt.xlabel(' Average SSIM',font={'family' : 'Times New Roman', 'size': 25})
plt.ylabel('Area [$um^2$]',font={'family' : 'Times New Roman', 'size': 25})
plt.yticks(fontproperties='Times New Roman', size=25)#设置大小及加粗
plt.xticks(fontproperties='Times New Roman', size=25)

plt.savefig("pic/dse_compare_gaussion_ssim_area_3w.png",bbox_inches = 'tight')
plt.savefig("pic/dse_compare_gaussion_ssim_area_3w.jpg",bbox_inches = 'tight')
plt.savefig("pic/dse_compare_gaussion_ssim_area_3w.svg",bbox_inches = 'tight')
# 显示图形
plt.show()



