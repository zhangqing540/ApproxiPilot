import numpy as np
import math
import  random
from  PIL import  Image
import cv2
def calculate_zi(Gi,X):
    sumi=np.zeros(len(X[0]))
    for each in Gi:
        sumi+=X[each]
    sumi/=(len(Gi)+0.000000001)
    zi=sumi
    return zi


def single_img_read(file_path):
    im = Image.open(file_path)
    img = im.load()
    im.close()
    height = im.size[0]
    width = im.size[1]
    x = []
    for i in range(0, height):
        for j in range(0, width):
            x.append(np.array(img[i, j]))
    return x,height,width
def dataset_in(path):
    with open(path,"r") as file:
        lines=file.readlines()
    dataset=[]
    for single in lines:
        single_design=single.strip().split(" ")
        dataset.append(single_design)
    #print(dataset)
    return dataset