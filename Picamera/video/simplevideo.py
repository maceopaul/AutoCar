import cv2
from picamera2 import Picamera2
import time

dispW=640
dispH=480

picam2 = Picamera2()
picam2.preview_configuration.main.size = (dispW,dispH)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.controls.FrameRate=30
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()
fps=0
pos=(30,60)
font=cv2.FONT_HERSHEY_SIMPLEX
height=1.5
weight=3
myColor=(0,0,255)

while True:
    width= 0
    height= 0
    tStart=time.time()
    frame= picam2.capture_array()
    
    #frame=cv2.flip(frame,-1)
    frame=cv2.flip(frame,1)
    frameGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame', frame)
    cv2.imshow('gray', frameGray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    tEnd=time.time()
    loopTime=tEnd-tStart
    fps=.9*fps + .1*(1/loopTime)
cv2.destroyAllWindows()
