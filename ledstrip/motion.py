
from gpiozero import MotionSensor
#
from board import SCL, SDA
import busio
import time
import datetime #new

from adafruit_pca9685 import PCA9685
i2c_bus = busio.I2C(SCL, SDA)
pca = PCA9685(i2c_bus)
pca.frequency = 60
#
pir = MotionSensor(17)
timedelay = 30 
printstart_time = "" 

while True:
    pir.wait_for_motion()
    start_time=time.time()
    printstart_time=time.time()
#    printstart_time=datetime.date.today()
#    printstart_time=datetime.datetime.today()
    print("The room is occupied. " + str(printstart_time))
    pca.channels[0].duty_cycle=0xFFFF
    pca.channels[1].duty_cycle=0xFFFF
    pca.channels[2].duty_cycle=0xFFFF
    pca.channels[3].duty_cycle=0xFFFF
    pca.channels[4].duty_cycle=0xFFFF
    pca.channels[5].duty_cycle=0xFFFF
    pca.channels[6].duty_cycle=0xFFFF
    pca.channels[7].duty_cycle=0xFFFF
    pca.channels[12].duty_cycle=0xFFFF
    pca.channels[13].duty_cycle=0xFFFF
    pca.channels[14].duty_cycle=0xFFFF
    pca.channels[15].duty_cycle=0xFFFF
  
    pir.wait_for_no_motion()
    end_time=time.time()
    if (end_time - time.time()) > 10.0:
        print("The room is unoccupied. ")

    pca.channels[0].duty_cycle=0x0
    pca.channels[1].duty_cycle=0x0
    pca.channels[2].duty_cycle=0x0
    pca.channels[3].duty_cycle=0x0
    pca.channels[4].duty_cycle=0x0
    pca.channels[5].duty_cycle=0x0
    pca.channels[6].duty_cycle=0x0
    pca.channels[7].duty_cycle=0x0
    pca.channels[12].duty_cycle=0x0
    pca.channels[13].duty_cycle=0x0
    pca.channels[14].duty_cycle=0x0
    pca.channels[15].duty_cycle=0x0

#    if (end_time - time.time()) > 15.0:
#        print("The room is unoccupied. ")
#
#        pca.channels[1].duty_cycle=0xFFFF
#        pca.channels[4].duty_cycle=0xFFFF
#        pca.channels[7].duty_cycle=0xFFFF
#        pca.channels[14].duty_cycle=0xFFFF
#        time.sleep(10)
#        pca.channels[1].duty_cycle=0x0
#        pca.channels[4].duty_cycle=0x0
#        pca.channels[7].duty_cycle=0x0
#        pca.channels[14].duty_cycle=0x0
