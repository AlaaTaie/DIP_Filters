import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('D:\Semester_6\Image Processing\Test.png', 0)

def Bilinear(image, scale):
    height, width = image.shape
    new_width = int(width * scale)
    new_height = int(height * scale)
    
    new_image = np.zeros((new_height, new_width), dtype=np.uint8)
    for i in range(new_height):
        for j in range(new_width):
            x = j / scale
            y = i / scale
            
            x1 = int(x)
            y1 = int(y)
            x2 = min(x1 + 1, width - 1)
            y2 = min(y1 + 1, height - 1)
            
            dx = x - x1
            dy = y - y1
            
            interpolated_value = (1 - dx) * (1 - dy) * image[y1, x1] + dx * (1 - dy) * image[y1, x2]+ (1 - dx) * dy * image[y2, x1]+ dx * dy * image[y2, x2]
            
            new_image[i, j] = min(max(int(interpolated_value), 0), 255)
            
    return new_image




scale = 2  
Interpolation = Bilinear(image, scale)

plt.imshow(Interpolation, cmap='gray')
plt.show()
