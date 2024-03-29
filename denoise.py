import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images/before_sunrise_low.jpg')

res = cv2.fastNlMeansDenoisingColored(img, None, 6,10,9,21)


cv2.imwrite('results/denoised_img.jpg',res)
cv2.imshow('result', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
