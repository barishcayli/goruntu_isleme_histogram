import cv2
import numpy as np
import matplotlib.pyplot as plt

resim = cv2.imread("resim.jpg",0)

def hesaplama(image):
    histogram = np.zeros((256,), dtype=int)
    yukseklik, genislik = image.shape

    
    for i in range(yukseklik):
        for j in range(genislik):
            degisken = image[i, j]
            histogram[degisken] += 1

    return histogram



histogram = hesaplama(resim)

plt.plot(histogram)
plt.title('Gri Resim Histogramı')
plt.xlabel('Piksel Değeri')
plt.ylabel('Piksel Sayısı')
plt.show()



cv2.waitKey()
cv2.destroyAllWindows()