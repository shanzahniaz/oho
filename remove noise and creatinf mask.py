import cv2
import numpy as np
img= cv2.imread('bird.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('Original image',img)
cv2.imshow('HSV image', hsv)
#CONVERT IN TO MASK
low_green=np.array([23,52,72])
high_green=np.array([102,255,255])
mask=cv2.inRange(hsv, low_green, high_green)
cv2.imshow('Masked Frame',mask)
cv2.waitKey(0)
# find contoure(shape outliners)
contours,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,0,255),2)
for c in contours:
    area=cv2.contourArea(c)
cv2.imshow('img',img)
cv2.destroyAllWindows()