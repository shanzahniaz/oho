import numpy as np
import cv2

img=cv2.imread('messi.jpg')
img2=cv2.imread('123.jpg')

print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)

img=cv2.merge((b,g,r))
cv2.imshow('',img)
cv2.waitKey(0)

img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))


ball=img[410:510,430:530]
img[10:110,120:202] = ball

#dst = cv2.add(img,img2)
dst=cv2.addWeighted(img,.9,img2,.1,0)
cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()