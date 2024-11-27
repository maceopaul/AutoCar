# %%
"""
/**
* @par Copyright (C): 2010-2020, Shenzhen Yahboom Tech
* @file:         IR control car.ipynb
* @author:       xiaozhen
* @version:      V1.0
* @date:         2020.09.24
* @brief:        IR control car
* @details
* @par History:  Description below
*/
"""

# %%
"""
### Import library
"""

# %%
#!/usr/bin/python3
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
import YB_Pcb_Car   

car = YB_Pcb_Car.YB_Pcb_Car()

# %%
"""
### Define the pins.
### Set the coding method of GPIO and initial settings.
"""

# %%
PIN = 36; #Define IR pin
buzzer = 32; #Define buzzer pin

#Set the GPIO port to BIARD encoding mode
GPIO.setmode(GPIO.BOARD)

#Ignore the warning message
GPIO.setwarnings(False)

ir_repeat_cnt = 0

def init():
    GPIO.setup(PIN,GPIO.IN,GPIO.PUD_UP)  #The pin of the red external device needs to be set to input pull-up
    GPIO.setup(buzzer,GPIO.OUT)         #Buzzer pin be set to output mode
    
    print("IR control start...")

#whistle
def whistle():
    p = GPIO.PWM(buzzer, 440)
    p.start(50)
    time.sleep(0.5)
    p.stop() 

# %%
"""
### The function exec_cmd defines the function of all the buttons on the infrared remote control.
### Here we only define some key functions. Users can add functions by themselves.
"""

# %%
def exec_cmd(key_val):
    if key_val==0x45:  #Power button
        car.Ctrl_Servo(1, 90)
        car.Ctrl_Servo(2, 90)
        car.Car_Stop()
    elif key_val==0x40:   #+ button
        car.Car_Run(100, 100)   #car advance
    elif key_val==0x15:   #Stop button
        car.Car_Stop()
    elif key_val==0x07:   #Left button
        car.Car_Left(100, 100)
    elif key_val==0x47:   #MENU button
        whistle()         #buzzer whistle
    elif key_val==0x09:   #Right button
        car.Car_Right(100, 100)
    elif key_val==0x16:   #0 button
        car.Car_Spin_Left(100, 100)
    elif key_val==0x19:   #- button
        car.Car_Back(100, 100)  
    elif key_val==0x0d:   #C button
        car.Car_Spin_Right(100, 100)
    elif key_val==0x0c:   #1 button
        car.Ctrl_Servo(1, 0)
    elif key_val==0x18:   #2 button
        car.Ctrl_Servo(1, 90)
    elif key_val==0x5e:   #3 button
        car.Ctrl_Servo(1, 180)
    elif key_val==0x08:   #4 button
        car.Ctrl_Servo(2, 0)
    elif key_val==0x1c:   #5 button
        car.Ctrl_Servo(2, 90)
    elif key_val==0x5a:   #6 button
        car.Ctrl_Servo(2, 180)
    else:
        print(key_val)
        print("no cmd")
        
    

# %%
"""
### Main process
"""

# %%
try:
    init()
    while True:
        if GPIO.input(PIN) == 0:
            ir_repeat_cnt = 0;
            count = 0
            while GPIO.input(PIN) == 0 and count < 200:
                count += 1
                time.sleep(0.00006)

            count = 0
            while GPIO.input(PIN) == 1 and count < 80:
                count += 1
                time.sleep(0.00006)

            idx = 0
            cnt = 0
            data = [0,0,0,0]
            for i in range(0,32):
                count = 0
                while GPIO.input(PIN) == 0 and count < 15:
                    count += 1
                    time.sleep(0.00006)

                count = 0
                while GPIO.input(PIN) == 1 and count < 40:
                    count += 1
                    time.sleep(0.00006)

                if count > 9:
                    data[idx] |= 1<<cnt
                if cnt == 7:
                    cnt = 0
                    idx += 1
                else:
                    cnt += 1
            if data[0]+data[1] == 0xFF and data[2]+data[3] == 0xFF:
                print("Get the key: 0x%02x" %data[2])
                exec_cmd(data[2])
        else:
            if ir_repeat_cnt > 110: #Judge whether the infrared remote control button is released, because the repetition cycle time is 110ms, so here it should be set to 110*0.001.
                ir_repeat_cnt = 0
                car.Car_Stop()
            else:
                time.sleep(0.001)
                ir_repeat_cnt += 1
except KeyboardInterrupt:
    pass
print("Ending")
GPIO.cleanup()

# %%
"""
### When you need to end the entire program, please click the square button (Interrupt the kernel) in the upper menu bar.
### Then you can see the Ending prompt, which means the program has been successfully ended
"""

# %%
