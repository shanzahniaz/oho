import numpy as np
import cv2
img=np.zeros((512,512,3),np.uint8)
img1=cv2.rectangle(img,(200,0),(300,100),(255,255,255),-1)
img2=cv2.imread('black and white.png')
#bitAnd=cv2.bitwise_and(img2,img1)
#bitor=cv2.bitwise_or(img2,img1)
#bitXor=cv2.bitwise_xor(img1,img2)
bitNot=cv2.bitwise_not(img1)
bitNot2=cv2.bitwise_not(img2)
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.waitKey(0)
#cv2.imshow('bitAnd',bitAnd)
#cv2.imshow('bitXor',bitXor)
cv2.imshow('bitNot1',bitNot1)
cv2.imshow('bitNot2',bitNot2)
cv2.waitKey(0)