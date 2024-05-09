import matplotlib.pyplot as plt

def build_histogram(file_path):
    # 从文件中读取浮点数列表
    with open(file_path, 'r') as file:
        data = [float(line.strip()) for line in file]

    # 获取最大值和最小值
    min_value = min(data)
    max_value = max(data)

    # 计算直方图的边界
    num_bins = 100  # 直方图的柱子数量
    bin_width = (max_value - min_value) / num_bins
    bins = [min_value + i * bin_width for i in range(num_bins+1)]

    # 绘制直方图
    plt.hist(data, bins=bins, edgecolor='black')

    # 设置图表标题和标签
    plt.title('Histogram')
    plt.xlabel('latency')
    plt.ylabel('Frequency')

    # 显示直方图
    plt.show()

# 调用函数并传入txt文件路径
file_path = "gaussion/gase/10w/latency_target.txt"  # 将文件名替换为你的txt文件路径
build_histogram(file_path)
