import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('D:\Semester_6\Image Processing\img.jpg', 0)

def NearestNeighbour(image,scale):
    height, width = image.shape
    new_height = int(height * scale)
    new_width = int(width * scale)
    scaled_image = np.zeros((new_height, new_width), dtype=np.uint8)
    for i in range(new_height):
        for j in range(new_width):
            scaled_image[i, j] = image[int(i/scale)][int(j/scale)]
    return scaled_image

scale = 5
Result = NearestNeighbour(image,scale)
plt.imshow(Result, cmap='gray')
plt.show()