import numpy as np
import cv2

image = cv2.imread('images/lalaland.jpg')
img = image.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


#range of yellow color hsv
lower = np.array([10, 116, 40], dtype='uint8')
upper = np.array([38, 255, 255], dtype='uint8')

#threshold the hsv img to only get yellow colors
mask = cv2.inRange(img, lower, upper)

#bitwise_and mask and orginal image
res = cv2.bitwise_and(image,image,mask=mask)
cv2.imwrite('results/yellow_dress.jpg',res)

cv2.imshow('image', image)
cv2.imshow('result', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
