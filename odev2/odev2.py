import cv2
import numpy as np

def geri(x):
    pass

cv2.namedWindow('HSV Ayarlayici')



cv2.createTrackbar('Hue Min', 'HSV Ayarlayici', 0, 179, geri)
cv2.createTrackbar('Saturation Min', 'HSV Ayarlayici',101, 255, geri)
cv2.createTrackbar('Value Min', 'HSV Ayarlayici', 101, 255, geri)
cv2.createTrackbar('Hue Max', 'HSV Ayarlayici', 11, 179, geri)
cv2.createTrackbar('Saturation Max', 'HSV Ayarlayici', 255, 255, geri)
cv2.createTrackbar('Value Max', 'HSV Ayarlayici', 255, 255, geri)

kamera = cv2.VideoCapture(0)

while True:
    ret, frame = kamera.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hm= cv2.getTrackbarPos('Hue Min', 'HSV Ayarlayici')
    sm = cv2.getTrackbarPos('Saturation Min', 'HSV Ayarlayici')
    vm = cv2.getTrackbarPos('Value Min', 'HSV Ayarlayici')
    h = cv2.getTrackbarPos('Hue Max', 'HSV Ayarlayici')
    s = cv2.getTrackbarPos('Saturation Max', 'HSV Ayarlayici')
    v = cv2.getTrackbarPos('Value Max', 'HSV Ayarlayici')

    #kırmızı için en düşük değerler h=0 s=101 v= 101
    en_dusuk = np.array([hm, sm, vm])
    #kırmızı için değerler h=11 s=255 v=255 
    en_yuksek = np.array([h, s, v])
    mask = cv2.inRange(hsv, en_dusuk, en_yuksek)

    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)
    
    alt_kirmizi = np.array([hm, sm, vm])
    ust_kirmizi = np.array([h, s, v])

    mask = cv2.inRange(hsv, alt_kirmizi, ust_kirmizi)

    sonuc = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('kirmizi nesneler (cikmak icin "x" e basiniz)', sonuc)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break



kamera.release()
cv2.destroyAllWindows()
