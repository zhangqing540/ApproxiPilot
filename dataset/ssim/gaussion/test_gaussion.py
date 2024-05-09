'''
#####################################################################
############           readme            ############################
operation :gaussion
this code is to get ssim in the DSE
library set
unsigned_8bit
add8u_1HG,add8u_6PT,add8u_0NS,add8u_0NQ,add8u_0NH,add8u_0PA,add8u_6MZ,add8u_0PL,add8u_0UK,add8u_05G,add8u_6LG,add8u_2J3,add8u_2AM
,add8u_0D0,add8u_4M7,add8u_3RE,add8u_0E2,add8u_2LL,add8u_6TH,add8u_02Y,add8u_108,add8u_6P8,add8u_6K6,add8u_0JM
,add8u_6S4,add8u_6R6,add8u_00M,add8u_6SM,add8u_0TP
unsigned_9bit
9_2,9_5,9_7,9_8,9_10,9_4,9_6,9_9,9_11,9_14,9_15,9_16,9_17,9_18,9_19,9_20
sub10bit
1,2,3,4,5,6,7,8,9,10
sample1=[3, 11, 2, 9, 12, 8, 10, 4, 13] [2, 4, 0, 5, 10, 6, 11, 9, 8] [5, 15, 1, 4, 0, 13, 11, 7, 9] [7, 12, 1, 2, 8, 13, 15, 5, 0]
sample=[]

#####################################################################
'''
import time
import threading
import multiprocessing
import numpy as np
import cv2
import glob
import skimage

from basic_module.basic_module import img_show,OIS,ODS,AP
from skimage.metrics import structural_similarity as ssim
import os
from PIL import Image
from main_operation.gaussion import gaussion
import queue
from basic_module.basic_module import *
if __name__ == '__main__':
    dataset_path="result/dataset_gaussion_deepapprox_20w.txt"
    input_data=dataset_in(dataset_path)
    input_q = multiprocessing.Queue()
    output_q = multiprocessing.Queue()
    for inputs in input_data:
        input_q.put(inputs)
    #pbar = tqdm(total=len(input_data), desc='Processing')
    pool = multiprocessing.Pool(processes=256)
    results = pool.starmap(gaussion,input_data)
    pool.close()
    pool.join()
    while not output_q.empty():
        results.append(output_q.get())
    with open('result/gaussion_20w_deepapprox_result_out.txt', 'w') as f:
        for r in results:
            f.write(str(r) + '\n')
    print("end_all")