import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# 读取第一个txt文件
target="../result/label.txt"
output="../result/pred.txt"
target_latency=[]
output_latency=[]
with open(target, 'r') as file1:
    for line in file1:
        values=line.split()
        target_latency.append(float(values[0]))
# 读取第二个txt文件
with open(output, 'r') as file2:
    for line in file2:
        values=line.split()
        output_latency.append(float(values[0])*200)
# 转换为浮点数
#area
for i,(elem1, elem2) in enumerate(zip(target_latency, output_latency)):
    diff = abs(elem1 - elem2)
    if diff > 0.5:
        print(f"index {i}:target {elem1} and output{elem2}, Difference: {diff}")
# 创建散点图
plt.scatter(target_latency, output_latency, label='Data Points',s=4)
#sns.kdeplot(x=target_latency,y=output_latency)
# 画出x=y的直线
plt.plot(target_latency, target_latency, color='red', label='target=output')

# 设置图例和标签
plt.legend()
plt.xlabel('area_target')
plt.ylabel('area_output')

# 显示图形
plt.show()
