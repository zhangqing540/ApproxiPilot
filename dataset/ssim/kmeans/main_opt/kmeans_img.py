'''
#####################################################################
############           readme            ############################
operation :gaussion
this code is to get ssim in the DSE
library set
unsigned_8bit
add8u_1HG,add8u_6PT,add8u_0NS,add8u_0NQ,add8u_0NH,add8u_0PA,add8u_6MZ,add8u_0PL,add8u_0UK,add8u_05G,add8u_6LG,add8u_2J3,add8u_2AM
,add8u_0D0,add8u_4M7,add8u_3RE,add8u_0E2,add8u_2LL,add8u_6TH,add8u_6FT,add8u_02Y,add8u_108,add8u_6P8,add8u_6K6,add8u_0JM,add8u_6QU
,add8u_6S4,add8u_6R6,add8u_00M,add8u_6SM,add8u_0TP
unsigned_9bit
9_2,9_5,9_7,9_8,9_10,9_4,9_6,9_9,9_11,9_14,9_15,9_16,9_17,9_18,9_19,9_20
sub10bit
1,2,3,4,5,6,7,8,9,10
#####################################################################
'''
import numpy as np
import cv2
import glob
import skimage
from skimage import io
from basic_module.kmeans_module import k_mean
from skimage.metrics import structural_similarity as ssim
import os
from PIL import Image
import math
import  random
import cv2
from basic_module.basic_module import single_img_read
ori_img="/home/zhangqing/approximate_opt/sim/kmeans/BSD/ori/"
acc_opt_img="/home/zhangqing/approximate_opt/sim/kmeans/BSD/acc_img/"
approx_opt_img="/home/zhangqing/approximate_opt/sim/kmeans/BSD/approx_img/"
num_class=2
#test in all pictures
#def gaussion(mul_81,mul_82,mul_83,mul_84,mul_85,mul_86,mul_87,mul_88,mul_89,add161,add162,add163,add164,add165,add166,add167,add168):
def kmeans(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r):
    opt_list=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r]
    #print(opt_list)
    acc_all=0
    for filename in os.listdir(ori_img):
        file_path=os.path.join(ori_img,filename)
        x,height,width=single_img_read(file_path)
        k_mean(x,num_class,height,width,filename,opt_list)
        acc = ssim(io.imread(approx_opt_img+filename), io.imread(acc_opt_img+filename),multichannel=True,channel_axis=2)
        acc_all=acc+acc_all
    ave_acc=acc_all
    #print("acc",ave_acc)
    return ave_acc
#opt_list=["sub2_8bit5","sub2_8bit5","sub2_8bit5","mul8u_4X5","mul8u_4X5","mul8u_4X5","add16u_15Q","add","mul11u_00H","sub2_8bit5","sub2_8bit5","sub2_8bit5","mul8u_4X5","mul8u_4X5","mul8u_4X5","add16u_15Q","add","mul11u_00H"]
#kmeans(opt_list)