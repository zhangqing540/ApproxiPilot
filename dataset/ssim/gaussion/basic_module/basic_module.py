import cv2
import numpy as np
def img_show(img):
    cv2.namedWindow("Image")
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def OIS(gt_edges, pred_edges, thresholds=[0.1, 0.3, 0.5, 0.7, 0.9]):
    """
    计算最优分割比率 (OIS)。
    参数：
        - gt_edges：真实边缘图像，灰度图像，像素值为 0 或 255。
        - pred_edges：预测边缘图像，灰度图像，像素值为 0 或 255。
        - thresholds：一组二值化阈值，用于将预测边缘图像转换为二值图像。
    返回：
        - OIS：最优分割比率。
    """

    # 计算真实边缘图像和预测边缘图像中的边缘像素数。
    n_gt_edges = np.sum(gt_edges == 255)
    n_pred_edges = np.sum(pred_edges == 255)

    # 初始化真正例、假正例和假反例的数量。
    tp_total = 0
    fp_total = 0
    fn_total = 0

    # 计算在每个阈值下的真正例、假正例和假反例的数量，并计算准确率和召回率。
    for threshold in thresholds:
        # 将预测边缘图像转换为二值图像。
        pred_edges_binary = cv2.threshold(pred_edges, threshold, 255, cv2.THRESH_BINARY)[1]

        # 计算真正例、假正例和假反例的数量。
        tp = np.sum(np.logical_and(gt_edges == 255, pred_edges_binary == 255))
        fp = np.sum(np.logical_and(gt_edges == 0, pred_edges_binary == 255))
        fn = np.sum(np.logical_and(gt_edges == 255, pred_edges_binary == 0))

        # 更新真正例、假正例和假反例的数量。
        tp_total += tp
        fp_total += fp
        fn_total += fn

    # 计算准确率和召回率。
    precision = tp_total / (tp_total + fp_total)
    recall = tp_total / (tp_total + fn_total)

    # 计算最优分割比率。
    OIS = 2 * precision * recall / (precision + recall)
    return OIS

def ODS(gt_edges, pred_edges, threshold=0.5):
    """
    计算最优分割比率 (ODS)。
    参数：
        - gt_edges：真实边缘图像，灰度图像，像素值为 0 或 255。
        - pred_edges：预测边缘图像，灰度图像，像素值为 0 或 255。
        - threshold：二值化阈值，用于将预测边缘图像转换为二值图像。
    返回：
        - ODS：最优分割比率。
    """

    # 将预测边缘图像转换为二值图像。
    pred_edges = cv2.threshold(pred_edges, threshold, 255, cv2.THRESH_BINARY)[1]

    # 计算真实边缘图像和预测边缘图像中的边缘像素数。
    n_gt_edges = np.sum(gt_edges == 255)
    n_pred_edges = np.sum(pred_edges == 255)

    # 计算真正例、假正例和假反例的数量。
    tp = np.sum(np.logical_and(gt_edges == 255, pred_edges == 255))
    fp = np.sum(np.logical_and(gt_edges == 0, pred_edges == 255))
    fn = np.sum(np.logical_and(gt_edges == 255, pred_edges == 0))

    # 计算准确率和召回率。
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)

    # 计算最优分割比率。
    ODS = 2 * precision * recall / (precision + recall)

    return ODS


def AP(gt_edges, pred_edges, threshold=0.5):
    """
    计算平均精度 (AP)。
    参数：
        - gt_edges：真实边缘图像，灰度图像，像素值为 0 或 255。
        - pred_edges：预测边缘图像，灰度图像，像素值为 0 或 255。
        - threshold：二值化阈值，用于将预测边缘图像转换为二值图像。
    返回：
        - AP：平均精度。
    """

    # 将预测边缘图像转换为二值图像。
    pred_edges = cv2.threshold(pred_edges, threshold, 255, cv2.THRESH_BINARY)[1]

    # 计算真实边缘图像和预测边缘图像中的边缘像素数。
    n_gt_edges = np.sum(gt_edges == 255)
    n_pred_edges = np.sum(pred_edges == 255)

    # 如果预测边缘图像中没有任何边缘像素，则精度为 0。
    if n_pred_edges == 0:
        return 0

    # 计算真实边缘图像中每个边缘像素的匹配分数。
    scores = gt_edges / 255 * pred_edges / 255

    # 按照匹配分数对边缘像素进行排序。
    sorted_indices = np.argsort(scores.flatten())[::-1]

    # 初始化计算变量。
    tp = 0  # 正确预测的边缘像素数。
    fp = 0  # 错误预测的边缘像素数。
    precision_sum = 0  # 精度的累计和。
    recall_sum = 0  # 召回率的累计和。
    last_recall = 0  # 上一个召回率的值。

    # 遍历排序后的边缘像素。
    for i in sorted_indices:
        # 如果当前像素为边缘像素，将 tp 加 1。
        if gt_edges.flatten()[i] == 255:
            tp += 1
        # 否则，将 fp 加 1。
        else:
            fp += 1

        # 计算当前的精度和召回率。
        precision = tp / (tp + fp)
        recall = tp / n_gt_edges

        # 如果当前的召回率大于上一个召回率的值，则将当前的精度累加到精度的累计和中。
        if recall > last_recall:
            precision_sum += precision
            last_recall = recall

        # 如果所有的边缘像素都被预测完了，则退出循环。
        if tp + fp == n_pred_edges:
            break

    # 计算平均精度。
    AP = precision_sum / n_gt_edges

    return AP
def dataset_in(path):
    with open(path,"r") as file:
        lines=file.readlines()
    dataset=[]
    for single in lines:
        single_design=single.strip().split(" ")
        dataset.append(single_design)
    #print(dataset)
    return dataset

