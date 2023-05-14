import cv2
import numpy as np

img = cv2.imread('C:/Users/night/Desktop/ToyotaChal/Hough/camera.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(gray, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 60, param1=111, param2=27, minRadius=0, maxRadius=130)
circles = np.uint16(np.around(circles))

for i in circles[0, :]:

    cv2.circle(img, (i[0], i[1]), i[2], (0,255,0), 2)

    cv2.circle(img, (i[0], i[1]), 2, (0,255,0), 3)

cv2.imshow("Circle Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()