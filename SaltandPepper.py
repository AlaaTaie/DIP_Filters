import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('D:\Semester_6\Image Processing\Test.png', 0)

def Salt_Pepper(image):
    height, width = image.shape
    pepper = 0.1  
    salt = 0.95  
    noise = np.zeros_like(image, dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            noise_val = np.random.random()
            if noise_val < pepper:
                noise[i][j] = 0  
            elif noise_val > salt:
                noise[i][j] = 255  
            else:
                noise[i][j] = image[i][j]  
    return noise


noise = Salt_Pepper(image)
S_P = noise + image

plt.imshow(S_P, cmap='gray')
plt.show()
