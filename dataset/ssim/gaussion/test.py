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
gaussion("mul8u_1A0M","mul8u_1A0M","mul8u_1A0M","mul8u_1A0M","mul8u_1A0M","mul8u_1A0M","mul8u_1A0M","mul8u_1A0M","mul8u_1A0M",
         "add16u_0C8","add16u_0C8","add16u_0C8","add16u_0C8","add16u_0C8","add16u_0C8","add16u_0C8","add16u_0C8")