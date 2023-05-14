# import the opencv library
import cv2
  
  
# define a video capture object
# the () indicates which feed to capture 0->laptop webcam  1->usb cam
vid = cv2.VideoCapture(1)
  
while(True):    
    # Capture the video frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('./camera.jpg', frame)
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()