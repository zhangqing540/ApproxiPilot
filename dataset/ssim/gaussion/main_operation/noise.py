import numpy as np
import random
import cv2

def salt_pepper_noise(image, ratio):
    output = np.zeros(image.shape, np.uint8)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):

            rand = random.random()
            if rand < ratio:  # salt pepper noise
                if random.random() > 0.5:  # change the pixel to 255
                    output[i][j] = 255
                else:
                    output[i][j] = 0
            else:
                output[i][j] = image[i][j]

    return output
image=cv2.imread("../BSD/ori/5096.jpg")
noisy_imgage=salt_pepper_noise(image,0.005)
cv2.imwrite("../BSD/gaussion/noise/5096.jpg", noisy_imgage)
denoised_image=cv2.GaussianBlur(noisy_imgage,(3,3),1)
cv2.imwrite("../BSD/gaussion/filter/5096.jpg", denoised_image)
cv2.imshow("image",denoised_image)
cv2.waitKey(0)