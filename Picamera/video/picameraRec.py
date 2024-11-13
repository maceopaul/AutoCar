

from picamera import PiCamera       
from time import sleep             

camera = PiCamera()                
camera.resolution= (640, 480)
camera.vflip = True
camera.hflip = True

camera.start_preview()             
sleep(2)                            

camera.start_recording("Myvideo.h264")
sleep(5)
camera.stop_recording()
