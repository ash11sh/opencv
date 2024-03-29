import cv2

#load image
img1 = cv2.imread('images/lalaland.jpg')
img2 = cv2.imread('images/lala.png')

#create roi
rows, cols, channels = img1.shape
roi = img2[0:rows,0:cols]

#create a mask
img2gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 100,255, cv2.THRESH_BINARY)

#create an inverse mask
mask_inv = cv2.bitwise_not(mask)

#blackout the masked region
img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)

#takeout masked region out
img1_fg = cv2.bitwise_and(img1,img1,mask=mask)

#put the masked region in ROI
dst = cv2.add(img1_bg,img1_fg)

img2[0:rows, 0:cols] = dst

cv2.imshow('result',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
