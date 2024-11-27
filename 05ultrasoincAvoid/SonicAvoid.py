

import RPi.GPIO as GPIO
import time
import YB_Pcb_Car    #导入Yahboom专门库文件

car = YB_Pcb_Car.YB_Pcb_Car()


GPIO.setmode(GPIO.BOARD)

#忽略警告信息
GPIO.setwarnings(False)

#定义超声波模块的引脚
EchoPin = 18
TrigPin = 16

GPIO.setup(EchoPin,GPIO.IN)
GPIO.setup(TrigPin,GPIO.OUT)

# %%
#超声波函数
def Distance():
    GPIO.output(TrigPin,GPIO.LOW)
    time.sleep(0.000002)
    GPIO.output(TrigPin,GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(TrigPin,GPIO.LOW)

    t3 = time.time()

    while not GPIO.input(EchoPin):
        t4 = time.time()
        if (t4 - t3) > 0.03 :
            return -1
    t1 = time.time()
    while GPIO.input(EchoPin):
        t5 = time.time()
        if(t5 - t1) > 0.03 :
            return -1

    t2 = time.time()
    #time.sleep(0.01)
    #print ("distance_1 is %d " % (((t2 - t1)* 340 / 2) * 100))
    return ((t2 - t1)* 340 / 2) * 100


# %%
def Distance_test():
    num = 0
    ultrasonic = []
    while num < 5:
            distance = Distance()
            #print("distance is %f"%(distance) )
            while int(distance) == -1 :
                distance = Distance()
                #print("Tdistance is %f"%(distance) )
            while (int(distance) >= 500 or int(distance) == 0) :
                distance = Distance()
                #print("Edistance is %f"%(distance) )
            ultrasonic.append(distance)
            num = num + 1
            #time.sleep(0.01)
    #print ('ultrasonic')
    distance = (ultrasonic[1] + ultrasonic[2] + ultrasonic[3])/3
    print("distance is %f"%(distance) ) 
    return distance



# %%
def avoid():
    distance = Distance_test()
    if distance < 15 :
        car.Car_Stop() 
        time.sleep(1)
        #car.Car_Spin_Right(100,100)
        car.Car_Back(50, 50)
        time.sleep(0.5)
    else:
        car.Car_Run(50,50) 

# %%
try:
    while True:
        avoid()
except KeyboardInterrupt:
    pass
car.Car_Stop() 
del car
print("Ending")
GPIO.cleanup()

