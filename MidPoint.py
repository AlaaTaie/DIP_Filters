import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('D:\Semester_6\Image Processing\img_e4417-bw.jpg', 0)

def MidPoint(image, window_size):
    height, width = image.shape
    filtered_image = np.zeros_like(image, dtype=np.float32)
    border = window_size // 2
    
    for i in range(border, height - border):
        for j in range(border, width - border):
            window = np.zeros((window_size, window_size), dtype=image.dtype)
            index = 0
            for m in range(window_size):
                for n in range(window_size):
                    window[m, n] = image[i - border + m, j - border + n]
                    index += 1
            Maximum= 0
            Minimum= 0
            for m in range(window_size):
                for n in range(window_size):
                    Maximum = max(Maximum, window[m, n])
                    Minimum = min(Minimum, window[m, n])
            filtered_image[i, j] = (Maximum+Minimum)/2

    return filtered_image

Mid = MidPoint(image,5)
plt.imshow(Mid, cmap='gray')
plt.show()