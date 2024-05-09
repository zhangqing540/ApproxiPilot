from skimage.metrics import structural_similarity as ssim
import skimage
from library.library import *
from ctypes import *
import ctypes
add9bit=CDLL("./library/add/9bit/add9.so")
#add9bit=CDLL("./library/add/sub10bit/sub.so")
opt="add9_10"
sum=add9bit.__dict__[opt].calc(ctypes.c_uint64(200), ctypes.c_uint64(6))
#sum =sub10_6(7,4)
print(sum)
#print(ssim("dataset/app.png","dataset/app2.png",multichannel=True))