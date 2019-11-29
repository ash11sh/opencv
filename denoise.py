import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images/before_sunrise_low.jpg')

res = cv2.fastNlMeansDenoisingColored(img, None, 10,10,7,21)


cv2.imshow('image', img)
cv2.imshow('result', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
