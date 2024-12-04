#Import the necessary Packages for this software to run
import mediapipe
import cv2

import RPi.GPIO as GPIO
import time
import YB_Pcb_Car    #导入Yahboom专门库文件

car = YB_Pcb_Car.YB_Pcb_Car()
print(car)

Tracking_Right1 = 11   #X1A  右边第一个传感器
Tracking_Right2 = 7  #X2A  右边第二个传感器
Tracking_Left1 = 13   #X1B 左边第一个传感器
Tracking_Left2 = 15   #X2B 左边第二个传感器

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(Tracking_Left1,GPIO.IN)
GPIO.setup(Tracking_Left2,GPIO.IN)
GPIO.setup(Tracking_Right1,GPIO.IN)
GPIO.setup(Tracking_Right2,GPIO.IN)

# %%
def tracking_function(handNum):
    Tracking_Left1Value = GPIO.input(Tracking_Left1);
    Tracking_Left2Value = GPIO.input(Tracking_Left2);
    Tracking_Right1Value = GPIO.input(Tracking_Right1);
    Tracking_Right2Value = GPIO.input(Tracking_Right2);
    
    if(handNum == 0):
            # 0 0 X 0
            # 1 0 X 0
            # 0 1 X 0        
        if (Tracking_Left1Value == False or Tracking_Left2Value == False) and  Tracking_Right2Value == False:
            car.Car_Spin_Right(70, 30)
            time.sleep(0.2)

            # 0 X 0 0       
            # 0 X 0 1 
            # 0 X 1 0       
        elif Tracking_Left1Value == False and (Tracking_Right1Value == False or  Tracking_Right2Value == False):
            car.Car_Spin_Left(30, 70) 
            time.sleep(0.2)
      
            # 0 X X X
        elif Tracking_Left1Value == False:
            car.Car_Spin_Left(70, 70) 
            time.sleep(0.05)
            
            # X X X 0        
        elif Tracking_Right2Value == False:
            car.Car_Spin_Right(70, 70)
            time.sleep(0.05)
            
            # X 0 1 X        
        elif Tracking_Left2Value == False and Tracking_Right1Value == True:
            car.Car_Spin_Left(60, 60) 
            time.sleep(0.02)
            
            # X 1 0 X          
        elif Tracking_Left2Value == True and Tracking_Right1Value == False:
            car.Car_Spin_Right(60, 60)
            time.sleep(0.02)
       
            # X 0 0 X        
        elif Tracking_Left2Value == False and Tracking_Right1Value == False:
            car.Car_Run(70, 70)
        print('Car Go')
    else:
        car.Car_Stop()
        print('Car Stop')
            

'''
#Use MediaPipe to draw the hand framework over the top of hands it identifies in Real-Time
drawingModule = mediapipe.solutions.drawing_utils
handsModule = mediapipe.solutions.hands

#Use CV2 Functionality to create a Video stream and add some values
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

#Add confidence values and extra settings to MediaPipe hand tracking. As we are using a live video stream this is not a static
#image mode, confidence values in regards to overall detection and tracking and we will only let two hands be tracked at the same time
#More hands can be tracked at the same time if desired but will slow down the system
with handsModule.Hands(static_image_mode=False, min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=2) as hands:
'''

#Create an infinite loop which will produce the live feed to our desktop and that will search for hands
def main():
    #Use MediaPipe to draw the hand framework over the top of hands it identifies in Real-Time
    drawingModule = mediapipe.solutions.drawing_utils
    handsModule = mediapipe.solutions.hands

    #Use CV2 Functionality to create a Video stream and add some values
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

    #Add confidence values and extra settings to MediaPipe hand tracking. As we are using a live video stream this is not a static
    #image mode, confidence values in regards to overall detection and tracking and we will only let two hands be tracked at the same time
    #More hands can be tracked at the same time if desired but will slow down the system
    handNum= -1;
    with handsModule.Hands(static_image_mode=False, min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=2) as hands:
        while True:
           ret, frame = cap.read()
           #Unedit the below line if your live feed is produced upsidedown
           #flipped = cv2.flip(frame, flipCode = -1)
           
           #Determines the frame size, 640 x 480 offers a nice balance between speed and accurate identification
           frame1 = cv2.resize(frame, (320, 240))
           
           #Produces the hand framework overlay ontop of the hand, you can choose the colour here too)
           results = hands.process(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))
           
           #In case the system sees multiple hands this if statment deals with that and produces another hand overlay
           if results.multi_hand_landmarks != None:
               for handLandmarks in results.multi_hand_landmarks:
                   drawingModule.draw_landmarks(frame1, handLandmarks, handsModule.HAND_CONNECTIONS)
               print('Point Count', len(results.multi_hand_landmarks))
               print('Hand')
               handNum= 1
           else:
               print('No hand')
               handNum= 0
                  #Below is Added Code to find and print to the shell the Location X-Y coordinates of Index Finger, Uncomment if desired
                  #for point in handsModule.HandLandmark:
                      
                      #normalizedLandmark = handLandmarks.landmark[point]
                      #pixelCoordinatesLandmark= drawingModule._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, 640, 480)
                      
                      #Using the Finger Joint Identification Image we know that point 8 represents the tip of the Index Finger
                      #if point == 8:
                          #print(point)
                          #print(pixelCoordinatesLandmark)
                          #print(normalizedLandmark)
            
           #Below shows the current frame to the desktop
               
           tracking_function(handNum)
           cv2.imshow("Frame", frame1);
           #key = cv2.waitKey(1) & 0xFF
           
           #Below states that if the |q| is press on the keyboard it will stop the system
           if cv2.waitKey(1) == ord("q"):
              break
        cv2.destroyAllWindows()
     
if __name__ == '__main__':
    main()
