import numpy as np
import math
import  random
from  PIL import  Image
import cv2
from skimage import io
from basic_module.basic_module import calculate_zi
from basic_module.kmeans_kernel import find_ci,find_ci_approx
iter_num=10
ori_img="/home/zhangqing/approximate_opt/sim/kmeans/BSD/ori/"
acc_opt_img="/home/zhangqing/approximate_opt/sim/kmeans/BSD/acc_img/"
approx_opt_img="/home/zhangqing/approximate_opt/sim/kmeans/BSD/approx_img/"
def k_mean(X,k,height,width,filename,opt_list):
    G=[] #G[i]={1,2,3...}表示属于第i类的样本在X中的索引，洗标
    Z=[] #Z[i] 第i类的中心点
    N=len(X)
    c=[] #c[i]=1,2,...,k；表示第i个样本属于第c[i]类
    tmpr=set()
    while len(Z)<k:
        r=random.randint(0,len(X)-1)#Randomly Initialize Cluster Centers
        if r not in tmpr:
            tmpr.add(r)
            Z.append(X[r])
            G.append(set())
    for i in range(N):
        c.append(0)
    #随机生成K个中心元素
    num=0
    while True:
        group_flag=np.zeros(k)
        for i in range(N):
            new_ci = find_ci_approx(X[i],Z,opt_list)
            if c[i] != new_ci:
                #找到了更好的,把xi从原来的c[i]调到new_ci去，于是有两个组需要更新：new_ci,c[i]
                if i in G[c[i]]:
                    G[c[i]].remove(i)
                group_flag[c[i]]=1  #把i从原来所属的组中移出来
                G[new_ci].add(i)
                group_flag[new_ci]=1    #把i加入到新的所属组去
                c[i]=new_ci
        #上面已经更新好了各元素的所属
        if num>iter_num:
            #没有组被修改
            break
        for i in range(k):
            if group_flag[i]==0:
                #未修改,无须重新计算
                continue
            else:
                Z[i]=calculate_zi(list(G[i]),X)
        #print(num)
        num+=1
    new_img=Image.new("RGB",(height,width))
    for i in range(0,height):
        for j in range(0,width):
            index = i * width + j
            pix = list(Z[c[index]])
            for k in range(len(pix)):
                pix[k]=int(pix[k])
            new_img.putpixel((i,j),tuple(pix))
    #new_img.show()
    new_img.save(approx_opt_img+filename)
    #io.imsave("../BSD/acc_img/"+filename,new_img)
    return new_img