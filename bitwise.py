import cv2

#load image
img1 = cv2.imread('images/lalaland.jpg')
img2 = cv2.imread('images/lala.png')

cv2.imshow('img_1',img1)
cv2.imshow('img_2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
