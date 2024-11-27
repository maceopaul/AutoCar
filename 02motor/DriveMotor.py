# %%
"""
/**
* @par Copyright (C): 2010-2020, Shenzhen Yahboom Tech
* @file:         驱动舵机
* @author:       xiaozhen
* @version：     V1.0
* @date:         2020.10.10
* @brief:        驱动舵机
* @details:
* @par History:  见如下说明
*/
"""

# %%
import YB_Pcb_Car  #导入亚博智能专用的底层库文件
import time

car = YB_Pcb_Car.YB_Pcb_Car()

print(car)

'''

#car.Car_Back(150, 150)
#time.sleep(2)
#car.Car_Stop()

car.Car_Left(0, 150)
time.sleep(1)
car.Car_Stop()



car.Car_Right(150, 0)
time.sleep(1)
car.Car_Stop()

car.Car_Left(0, 150)
time.sleep(1)
car.Car_Stop()
'''

# %%
car.Car_Run(150, 150)
time.sleep(2)
car.Car_Stop()

# %%
"""
###### 小车后退两秒
"""

# %%
car.Car_Back(150, 150)
time.sleep(2)
car.Car_Stop()

# %%
"""
###### 小车左转两秒
"""

# %%
car.Car_Left(0, 150)
time.sleep(2)
car.Car_Stop()

# %%
"""
###### 小车右转两秒
"""

# %%
car.Car_Right(150, 0)
time.sleep(2)
car.Car_Stop()

# %%
"""
###### 小车左旋两秒
"""

# %%
car.Car_Spin_Left(150, 150)
time.sleep(2)
car.Car_Stop()

# %%
"""
###### 小车右旋两秒
"""

# %%
car.Car_Spin_Right(150, 150)
time.sleep(2)
car.Car_Stop()

# %%
"""
###### 小车停止
"""

# %%
car.Car_Stop()

# %%
del car #The object needs to be released after use, otherwise, when the next program needs to use this object module, it will be occupied and will become unusable

# %%
