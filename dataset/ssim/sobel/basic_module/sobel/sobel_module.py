import numpy as np
import cv2
from basic_module.sobel.sobel_kernel import sobel_kernel
def sobel_v(img, threshold,opt1,opt2,opt3,opt4,opt5):
    rows = np.size(img, 0)
    columns = np.size(img, 1)
    mag = np.zeros(img.shape)
    for i in range(0, rows - 2):
        for j in range(0, columns - 2):
            v=sobel_kernel(i=i,j=j,img=img,opt1=opt1,opt2=opt2,opt3=opt3,opt4=opt4,opt5=opt5)
            #print("v",type(v))
            #exit(0)
            mag[i + 1, j + 1] = v
           # print("11",v,mag[i + 1, j + 1] )
           #exit(0)
    for p in range(0, rows):
        for q in range(0, columns):
            if mag[p, q] < threshold:
                mag[p, q] = 0

    return mag.astype(np.uint8)
def sobel_h(img, threshold):
    '''
    edge detection with the horizon Sobel filter

    Parameters
    ----------
    img : TYPE
        the image input.
    threshold : TYPE
         varies for application [0 255].

    Returns
    -------
    mag : TYPE
        output after edge detection.

    '''
    G_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    rows = np.size(img, 0)
    columns = np.size(img, 1)
    mag = np.zeros(img.shape)
    for i in range(0, rows - 2):
        for j in range(0, columns - 2):
            h = sum(sum(G_y * img[i:i + 3, j:j + 3]))  # horizon
            mag[i + 1, j + 1] = h

    for p in range(0, rows):
        for q in range(0, columns):
            if mag[p, q] < threshold:
                mag[p, q] = 0
    return mag
def sobel(img, threshold):
    '''
    edge detection based on sobel

    Parameters
    ----------
    img : TYPE
        the image input.
    threshold : TYPE
         varies for application [0 255].

    Returns
    -------
    mag : TYPE
        output after edge detection.

    '''
    G_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    G_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    rows = np.size(img, 0)
    columns = np.size(img, 1)
    mag = np.zeros(img.shape)
    for i in range(0, rows - 2):
        for j in range(0, columns - 2):
            v = sum(sum(G_x * img[i:i + 3, j:j + 3]))  # vertical
            h = sum(sum(G_y * img[i:i + 3, j:j + 3]))  # horizon
            mag[i + 1, j + 1] = np.sqrt((v ** 2) + (h ** 2))

    for p in range(0, rows):
        for q in range(0, columns):
            if mag[p, q] < threshold:
                mag[p, q] = 0
    return mag
