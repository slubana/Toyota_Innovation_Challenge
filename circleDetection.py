import cv2
import numpy as np
  
# Let's load a simple image with 3 black squares
image = cv2.imread('./Metal_1.jpg')
cv2.waitKey(0)

#Slicing using ROI #create 2 cropped images
cropped1 = image[250:550,0:200].copy()
cropped2 = image[250:550,1000:1310].copy()
croppedImages = []
croppedImages.append(cropped1)
croppedImages.append(cropped2)

for croppedImage in croppedImages:
    # Grayscale
    gray = cv2.cvtColor(croppedImage, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray', croppedImage)

    # Find Canny edges
    edged = cv2.Canny(gray, 30, 200,)
    cv2.waitKey(0)
    
    # Finding Contours
    # Use a copy of the image e.g. edged.copy()
    # since findContours alters the image
    contours, hierarchy = cv2.findContours(edged, 
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    circles = []
    for contour in contours:
        area = cv2.contourArea(contour)
        # gives area of contour
        perimeter = cv2.arcLength(contour, closed=True)
        # gives perimeter of contour

        borders = cv2.approxPolyDP(curve=contour,epsilon=0.05*perimeter,closed=True)
        # approximate boundaries for given polygon contour
        if len(borders) > 3 and area > 40 and area < 70:
            circles.append(contour)
            

# Draw all contours
# -1 signifies drawing all contours
cv2.drawContours(image, circles, -1, (0, 255, 0), 3)
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()