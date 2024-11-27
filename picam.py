
from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.start_preview()
sleep(2)
camera.capture('test.jpg')
camera.stop_preview() 


'''
import cv2 as cv

capture = cv.VideoCapture('vid.h264')
#fps = capture.get(cv.CAP_PROP_FPS)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    fps = capture.get(cv.CAP_PROP_FPS)
    
    if cv.waitKey(20) & 0xFF==ord('q'):
        break                              
        
capture.release()
cv.destroyAllWindows()
'''
