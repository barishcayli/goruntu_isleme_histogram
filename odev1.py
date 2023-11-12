import cv2
import numpy as np
import matplotlib.pyplot as plt

resim = cv2.imread("resim.jpg",0)

def calculate_histogram(image):
    histogram = np.zeros((256,), dtype=int)
    yukseklik, genislik = image.shape

    
    for i in range(yukseklik):
        for j in range(genislik):
            pixel_value = image[i, j]
            histogram[pixel_value] += 1

    return histogram



histogram = calculate_histogram(resim)

plt.plot(histogram)
plt.title('Gri Resim Histogramı')
plt.xlabel('Piksel Değeri')
plt.ylabel('Piksel Sayısı')
plt.show()



cv2.waitKey()
cv2.destroyAllWindows()