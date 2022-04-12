import cv2
import numpy as np

img = cv2.imread("senyum2.PNG")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gambar senyum2 original", img)
cv2.imshow("Gambar senyum2 Grayscale", gray)

cv2.waitKey(0)
cv2.destroyWindow()