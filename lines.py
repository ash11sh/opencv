import cv2
import numpy as np

#read image
img = cv2.imread('images/bill1.jpg')

#convert to gray
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#find edges
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

#probabilistic Hough transform algorithm for line detection
lines = cv2.HoughLinesP(edges,1,np.pi/180,120,minLineLength=25,maxLineGap=20)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imwrite('results/lines.jpg',img)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
