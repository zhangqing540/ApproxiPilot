#this code is to produce the test image
import numpy as np
import cv2
import os
from library.library import *
from basic_module.basic_module import img_show
def sobel_v(img, threshold):
    G_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    rows = np.size(img, 0)
    columns = np.size(img, 1)
    mag = np.zeros(img.shape)
    for i in range(0, rows - 2):
        for j in range(0, columns - 2):
            part1_sum1 = add(img[i + 2, j], img[i + 2, j + 2])
            part1_sum3 = add(img[i, j], img[i, j + 2])
            part1_sum2 = 2 * (img[i, j + 1])
            part1_sum4 = (2) * (img[i + 2, j + 1])
            part2_sum1 = add(part1_sum1, part1_sum2)
            part2_sum2 = add(part1_sum3, part1_sum4)
            v = sub(part2_sum1, part2_sum2)
            mag[i + 1, j + 1] = v

    for p in range(0, rows):
        for q in range(0, columns):
            if mag[p, q] < threshold:
                mag[p, q] = 0
    return mag
dir_path="/home/zq/simulator/BSDS500/BSDS500/images/test"
save_path="/home/zq/simulator/BSDS500/BSDS500/pred_edges/test/"
files=os.listdir(dir_path)
for file in files:
    img = cv2.imread(dir_path+"/"+file,0)
    img_v=sobel_v(img,50)
    #cv2.imshow("1",img_v)
    #cv2.waitKey(0)
    save_png=save_path+file[:-4]+'.png'
    cv2.imwrite(save_png,img_v)




