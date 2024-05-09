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
from basic_module.gaussion.gaussion_module import gaussian_filter
from basic_module.basic_module import img_show,OIS,ODS,AP
from skimage.metrics import structural_similarity as ssim
import os
from PIL import Image
result_folder_path="BSD/gaussion/filter"
test_folder_path="BSD/gaussion/noise"
#test in all pictures
def gaussion(mul_81,mul_82,mul_83,mul_84,mul_85,mul_86,mul_87,mul_88,mul_89,add161,add162,add163,add164,add165,add166,add167,add168):
      acc_all=0
      for filename in os.listdir(test_folder_path):
          file_path=os.path.join(test_folder_path,filename)
          #if the picture in the fold
          #print("name1",filename)
          if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
              img=cv2.imread(file_path)
              #cv2.imshow("image",img)
              #cv2.waitKey(0)
              img_v=gaussian_filter(img,mul_81,mul_82,mul_83,mul_84,mul_85,mul_86,mul_87,mul_88,mul_89,add161,add162,add163,add164,add165,add166,add167,add168)
              #cv2.imshow("image",img_v)
              #cv2.waitKey(0)
              for file in os.listdir(result_folder_path):
                  if file[:-4] == filename[:-4]:
                      img_path = os.path.join(result_folder_path,file)
                      real_edges=cv2.imread(img_path)
                      acc=ssim(real_edges,img_v,multichannel=True,channel_axis=2)
                      #print(acc)
          acc_all=acc+acc_all
      ave_acc=acc_all/2
      print("ing...")
      return ave_acc

