import cv2 as cv
import numpy as np
def nothing(x):
    pass
cv.namedWindow("Trackking")
while True:
    frame = cv.imread('balls.png')
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    l_b = np.array([110, 50, 50])
    u_b = np.array([130, 255, 255])
    mask = cv.inRange(hsv, l_b, u_b)
    res = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow("res", res)

    key = cv.waitKey(1)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()