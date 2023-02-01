
from gpiozero import MotionSensor
#
from board import SCL, SDA
import busio
import time

from adafruit_pca9685 import PCA9685
i2c_bus = busio.I2C(SCL, SDA)
pca = PCA9685(i2c_bus)
pca.frequency = 60
#
pir = MotionSensor(17)

while True:
    pir.wait_for_motion()
        
    #while waitingstill():
    for x in (8, 9, 10, 11):
        pca.channels[x].duty_cycle=0x7FFF
        pca.channels[x].duty_cycle=0xFFFF
        pca.channels[x].duty_cycle=0xFFFF
        pca.channels[x].duty_cycle=0xFFFF
        time.sleep(.0625)
        pca.channels[x].duty_cycle=0xFFFF
        pca.channels[x].duty_cycle=0x7FFF
        pca.channels[x].duty_cycle=0xFFFF
        pca.channels[x].duty_cycle=0xFFFF
        time.sleep(.0625)
        pca.channels[x].duty_cycle=0xFFFF
        pca.channels[x].duty_cycle=0xFFFF
        pca.channels[x].duty_cycle=0x7FFF
        pca.channels[x].duty_cycle=0xFFFF
        time.sleep(.0625)
        pca.channels[x].duty_cycle=0xFFFF
        pca.channels[x].duty_cycle=0xFFFF
        pca.channels[x].duty_cycle=0xFFFF
        pca.channels[x].duty_cycle=0x7FFF
        time.sleep(.0625)
    print("You moved")
    pir.wait_for_no_motion()

