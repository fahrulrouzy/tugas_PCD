import cv2

img = cv2.imread("pantai1.PNG", 0)

img_1 = 255 - img

cv2.imshow("Original Image", img)
cv2.imshow("Image Negative", img_1)

cv2.waitKey(0)
cv2.destroyWindow()