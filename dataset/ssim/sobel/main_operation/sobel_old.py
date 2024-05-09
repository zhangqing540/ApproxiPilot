'''
#####################################################################
############           readme            ############################
operation :sobel
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
import skimage
from basic_module.sobel.sobel_module import sobel,sobel_h,sobel_v
from basic_module.basic_module import img_show,OIS,ODS,AP
from skimage.metrics import structural_similarity as ssim
import os
from PIL import Image
#
img =cv2.imread("BSDS500/BSDS500/images/test/145059.jpg", 0)
img_test =cv2.imread("BSDS500/BSDS500/pred_edges/test/145059.jpg", 0)
#list 0D0 0E2 0JM 0NH 0NQ 00M 6LG 6PT 6SM 6TH 108
opt1="add8u_02Y"
opt2="add8u_02Y"
opt3="add9_8"
opt4="add9_10"
opt5="sub10_3"
img_v=sobel_v(img,50,opt1=opt1,opt2=opt2,opt3=opt3,opt4=opt4,opt5=opt5)
real_edges=cv2.imread(img_test, cv2.IMREAD_GRAYSCALE)
print(ssim(real_edges,img_v,multichannel=True))


'''
#####################################################################
############           readme            ############################
operation :sobel
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
from basic_module.sobel.sobel_module import sobel,sobel_h,sobel_v
from basic_module.basic_module import img_show,OIS,ODS,AP
from skimage.metrics import structural_similarity as ssim
import os
from PIL import Image
search_folder_path="BSDS500/BSDS500/pred_edges/test"
test_folder_path="BSDS500/BSDS500/images/test/"
#test in all pictures
for filename in os.listdir(test_folder_path):
    file_path=os.path.join(test_folder_path,filename)
    #if the picture in the fold
    print("name1",filename)
    if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        img=cv2.imread(file_path,0)
        opt1="add8u_02Y"
        opt2="add8u_02Y"
        opt3="add9_8"
        opt4="add9_10"
        opt5="sub10_3"
        img_v=sobel_v(img,50,opt1=opt1,opt2=opt2,opt3=opt3,opt4=opt4,opt5=opt5)
        for file in os.listdir(search_folder_path):
            if file[:-4] == filename[:-4]:
                # 如果找到了与filename相同的文件，打开该文件
                print("name2", file)
                img_path = os.path.join(search_folder_path, file)
                real_edges=cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                ssim=ssim(real_edges,img_v,multichannel=True)
                print("ssim",ssim)