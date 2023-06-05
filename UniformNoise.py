import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('D:\Semester_6\Image Processing\img.jpg', 0)

def Uniform(image):
    height, width = image.shape
    a = 0  
    b = 1 
    noise = np.zeros_like(image, dtype=np.uint8)  #unit8 np.zeros takes from 0 to 255
    for i in range(height):
        for j in range(width):
            noise[i][j] = np.random.random()
            if a <= noise[i][j] <= b:
                noise[i][j] = 1 / (b - a)
            else:
                noise[i][j] = 0
    return noise

noise = Uniform(image)
uni = noise + image

plt.imshow(uni, cmap='gray')
plt.show()
