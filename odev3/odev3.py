import cv2
import numpy as np

# Görüntüyü oku
goruntu = cv2.imread('resim.jpg')

# Görüntüyü gri seviyeye dönüştür
gri_ton = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)

# Gürültüyü azaltmak için Gauss filtresi uygula


# Görüntüyü eşikle (threshholding)
a, esik = cv2.threshold(gri_ton, 50, 255, cv2.THRESH_BINARY)

# Morfolojik işlemler (istenmeyen arka planları temizleme)
çekirdek = np.ones((5, 5), np.uint8)
esik = cv2.morphologyEx(esik, cv2.MORPH_OPEN, çekirdek, iterations=2)
esik = cv2.morphologyEx(esik, cv2.MORPH_CLOSE, çekirdek, iterations=2)

# Contour (sınırlar) bulma
sinir, a = cv2.findContours(esik, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Pirinç sayısı
pirinç_sayisi = len(sinir)


# Her bir pirinci sınırlayan dikdörtgenin içine sayı yazma
for i, kontur in enumerate(sinir):
    (x, y, w, h) = cv2.boundingRect(kontur)
    cv2.putText(goruntu, str(i+1), (x + w // 2 - 10, y + h // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Görüntü üzerine konturları çiz
cv2.drawContours(goruntu, sinir, -1, (0, 255, 0), 2)

# görütü boyutu ayarlama
cv2.namedWindow("{} adet pirinc bulunmakta".format(pirinç_sayisi),cv2.WINDOW_NORMAL)
cv2.namedWindow("normal goruntu",cv2.WINDOW_NORMAL)

# Görüntüleri ekrana göster
cv2.imshow('{} adet pirinc bulunmakta'.format(pirinç_sayisi), goruntu)
cv2.imshow('normal goruntu', esik)
cv2.waitKey(0)
cv2.destroyAllWindows()
