
import RPi.GPIO as GPIO
import time

Tracking_Left1 = 13   
Tracking_Left2 = 15   
Tracking_Right1 = 11  
Tracking_Right2 = 7   

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(Tracking_Left1,GPIO.IN)
GPIO.setup(Tracking_Left2,GPIO.IN)
GPIO.setup(Tracking_Right1,GPIO.IN)
GPIO.setup(Tracking_Right2,GPIO.IN)

print ('start')

try:
    while True:
        Tracking_Left1Value = GPIO.input(Tracking_Left1);
        Tracking_Left2Value = GPIO.input(Tracking_Left2);
        Tracking_Right1Value = GPIO.input(Tracking_Right1);
        Tracking_Right2Value = GPIO.input(Tracking_Right2);
        print ('Car Left: ',Tracking_Left1Value)
        print ('Car Center Left: ', Tracking_Left2Value)
        print ('Car Center Right: ', Tracking_Right1Value)
        print ('Car Right: ', Tracking_Right2Value)
        print ('---')
        time.sleep(1)
except KeyboardInterrupt:
    pass
print("Ending")
GPIO.cleanup()
