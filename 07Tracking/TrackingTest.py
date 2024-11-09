# %%
"""
/**
* @par Copyright (C): 2010-2020, Shenzhen Yahboom Tech
* @file:         巡线传感器测试
* @author:       xiaozhen
* @version：      V1.0
* @date:         2020.09.25
* @brief:       巡线传感器测试
* @details:
* @par History:  见如下说明
*/
"""

# %%
"""
### 运行如下所示的程序之后，你可以看到四个巡线传感器的引脚的状态会被打印出来。
#### 检测到黑线低电平指示灯点亮，未检测到黑线高电平指示灯熄灭。
"""

# %%
#-*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time

Tracking_Left1 = 13   #X1B 左边第一个传感器
Tracking_Left2 = 15   #X2B 左边第二个传感器
Tracking_Right1 = 11   #X1A  右边第一个传感器
Tracking_Right2 = 7  #X2A  右边第二个传感器

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
        print (Tracking_Left1Value)
        print (Tracking_Left2Value)
        print (Tracking_Right1Value)
        print (Tracking_Right2Value)
        print ('---')
        time.sleep(1)
except KeyboardInterrupt:
    pass
print("Ending")
GPIO.cleanup()

# %%


# %%
"""
### 当你需要结束整个程序时，请点击上方菜单栏中的方块型按钮(Interrupt the kernel）.
### 然后你可以看到Ending提示，表示已经成功地结束了这个程序
"""