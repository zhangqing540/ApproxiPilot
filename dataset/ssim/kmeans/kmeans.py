import time
import threading
import multiprocessing
import numpy as np
import cv2
import glob
import skimage
from skimage.metrics import structural_similarity as ssim
import os
from PIL import Image
from main_opt.kmeans_img import kmeans
import queue
from basic_module.basic_module import *
if __name__ == '__main__':
    dataset_path="result/dataset_kmeans_5w1.txt"
    input_data=dataset_in(dataset_path)
    input_q = multiprocessing.Queue()
    output_q = multiprocessing.Queue()
    for inputs in input_data:
        input_q.put(inputs)
    #pbar = tqdm(total=len(input_data), desc='Processing')
    pool = multiprocessing.Pool(processes=128)
    results = pool.starmap(kmeans,input_data)
    pool.close()
    pool.join()
    while not output_q.empty():
        results.append(output_q.get())
    with open('result/result_kmeans_5w1.txt', 'w') as f:
        for r in results:
            f.write(str(r) + '\n')
    print("end_all")