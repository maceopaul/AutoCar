# %%
"""
/**
* @par Copyright (C): 2010-2020, Shenzhen Yahboom Tech
* @file:         Restricting_test
* @author:       xiaozhang
* @version：     V1.0
* @date:         2020.11.24
* @brief:        画地为牢实验
* @details:
* @par History:  见如下说明
*/
"""

# %%
"""
### 运行如下所示的程序之后，
"""

# %%
#-*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time
import YB_Pcb_Car    #导入Yahboom专门库文件

car = YB_Pcb_Car.YB_Pcb_Car()

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
#画地为牢功能函数
def restricting():
    Tracking_Left1Value = GPIO.input(Tracking_Left1);
    Tracking_Left2Value = GPIO.input(Tracking_Left2);
    Tracking_Right1Value = GPIO.input(Tracking_Right1);
    Tracking_Right2Value = GPIO.input(Tracking_Right2);
     
        # 0000
    if Tracking_Left1Value == False and Tracking_Left2Value == False and Tracking_Right1Value == False and Tracking_Right2Value == False :
        car.Car_Spin_Right(75,75) 
        time.sleep(1)
        #1X00
    elif Tracking_Left1Value == True and Tracking_Right1Value == False and Tracking_Right2Value == False :
        car.Car_Spin_Left(70,70) 
        time.sleep(1)
        #00X1
    elif Tracking_Left1Value == False and Tracking_Left2Value == False and Tracking_Right2Value == True :
        car.Car_Spin_Right(70,70)
        time.sleep(1)
        #10X1
    elif Tracking_Left1Value == True and Tracking_Left2Value == False and Tracking_Right2Value == True :
        car.Car_Spin_Right(70,70) 
        time.sleep(1)
        #1X01
    elif Tracking_Left1Value == True and Tracking_Right1Value == False and Tracking_Right2Value == True :
        car.Car_Spin_Right(70,70) 
        time.sleep(1)    
        #0110
    elif Tracking_Left1Value == False and Tracking_Left2Value == True and Tracking_Right1Value == True and Tracking_Right2Value == False :
        car.Car_Spin_Right(70,70) 
        time.sleep(1)
        #0111
    elif Tracking_Left1Value == False and Tracking_Left2Value == True and Tracking_Right1Value == True and Tracking_Right2Value == True :
        car.Car_Spin_Right(50,50) 
        time.sleep(1)
        #1110
    elif Tracking_Left1Value == True and Tracking_Left2Value == True and Tracking_Right1Value == True and Tracking_Right2Value == False :
        car.Car_Spin_Left(50,50) 
        time.sleep(1)
    elif Tracking_Left1Value == True and Tracking_Left2Value == True and Tracking_Right1Value == True and Tracking_Right2Value == True :
        car.Car_Run(70,70) 


# %%
try:
    while True:
        restricting()
except KeyboardInterrupt:
    pass
car.Car_Stop() 
del car
print("Ending")
GPIO.cleanup()

# %%
"""
### 当你需要结束整个程序时，请点击上方菜单栏中的方块型按钮(Interrupt the kernel）.
### 然后你可以看到Ending提示，表示已经成功地结束了这个程序
"""

# %%
