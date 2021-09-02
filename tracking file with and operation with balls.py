
import cv2 as cv
import numpy as np
def nothing(x):
    pass
cv.namedWindow("Tracking")
cv.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv.createTrackbar("US", "Tracking", 255, 255, nothing)
cv.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    frame = cv.imread('balls.png')
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    l_h = cv.getTrackbarPos("LH", "Tracking")
    l_s = cv.getTrackbarPos("LS", "Tracking")
    l_v = cv.getTrackbarPos("LV", "Tracking")

    U_h = cv.getTrackbarPos("UH", "Tracking")
    U_s = cv.getTrackbarPos("US", "Tracking")
    U_v = cv.getTrackbarPos("UV", "Tracking")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([U_h, U_s, U_v])
    mask = cv.inRange(hsv, l_b, u_b)
    res = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow("res", res)
    key = cv.waitKey(1)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destryAllWindows()