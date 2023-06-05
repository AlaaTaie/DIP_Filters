import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('D:\Semester_6\Image Processing\img_e4417-bw.jpg', 0)

def AlphaTrimmed(image, window_size, alpha):
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
            
            sorted_window = np.sort(window, axis=None)
            # Trim the extreme values based on alpha
            trimmed_values = sorted_window[alpha:len(sorted_window) - alpha]
            # Calculate the mean of the trimmed values
            mean = np.sum(trimmed_values) / len(trimmed_values)
            filtered_image[i, j] = mean

    return filtered_image

Alpha = AlphaTrimmed(image,7, 3)
plt.imshow(Alpha, cmap='gray')
plt.show()