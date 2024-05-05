import numpy as np
import matplotlib.pyplot as plt

# 读取第一个txt文件
target="../result/sobel_4k/latency_output.txt"
output="../result/sobel_4k/latency_target.txt"
#target="laplace/gsae/ssim_output.txt"
#output="laplace/gsae/ssim_target.txt"
with open(target, 'r') as file1:
    lines1 = file1.readlines()

# 读取第二个txt文件
with open(output, 'r') as file2:
    lines2 = file2.readlines()

# 转换为浮点数
#area
x = np.array([(float(line.strip())) for line in lines1])
y = np.array([(float(line.strip())) for line in lines2])

# 创建散点图
plt.scatter(x, y, label='Data Points',s=4)

# 画出x=y的直线
plt.plot(x, x, color='red', label='target=output')

# 设置图例和标签
plt.legend()
plt.xlabel('latency_target')
plt.ylabel('latency_output')

# 显示图形
plt.show()
