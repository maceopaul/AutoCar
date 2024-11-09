import YB_Pcb_Car
import time

car = YB_Pcb_Car.YB_Pcb_Car()

car.Car_Run(150,150)
time.sleep(1)
#car.Car_Stop()

car.Car_Back(150, 150)
time.sleep(1)
#car.Car_Stop()

car.Car_Left(0,150)
time.sleep(1)
#car.Car_Stop()

car.Car_Right(150,0)
time.sleep(1)
#car.Car_Stop()

car.Car_Stop()



