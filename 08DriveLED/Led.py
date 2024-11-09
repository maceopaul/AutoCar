# %%
"""
/**
* @par Copyright (C): 2010-2020, Shenzhen Yahboom Tech
* @file:         驱动LED.ipynb
* @author:       xiaozhen
* @version：     V1.0
* @date:         2020.10.14
* @brief:        驱动LED
* @details:
* @par History:  见如下说明
*/
"""

# %%
#-*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time

#设置引脚编码方式为BOARD编码方式
GPIO.setmode(GPIO.BOARD)

#忽略警告
GPIO.setwarnings(False)

LED1 = 40   #定义LED1(红色)的引脚
LED2 = 38   #定义LED2(蓝色)的引脚

# %%
"""
###### 设置LED1,LED2的引脚为输出模式
"""

# %%
GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)

# %%
"""
###### 点亮
"""

# %%
GPIO.output(LED1, GPIO.HIGH)
GPIO.output(LED2, GPIO.HIGH)
time.sleep(5)

# %%
"""
###### 两个LED熄灭
"""

# %%
GPIO.output(LED1, GPIO.LOW)
GPIO.output(LED2, GPIO.LOW)

# %%
