# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# This simple test outputs a 50% duty cycle PWM single on the 0th channel. Connect an LED and
# resistor in series to the pin to visualize duty cycle changes and its impact on brightness.

from board import SCL, SDA
import busio
import time

# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685

# Create the I2C bus interface.
i2c_bus = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c_bus)

# Set the PWM frequency to 60hz.
pca.frequency = 60

low = 0x3FFF #Low 16383
med = 0x7FFF #Medium 32767
hi = 0xFFFF #High 65535

brightness =  low
Test = low

# Set the PWM duty cycle for channel zero to 50%. duty_cycle is 16 bits to match other PWM objects
# but the PCA9685 will only actually give 12 bits of resolution.
#MODDED BY RON

while True:
    pca.channels[0].duty_cycle = 0x0000 #Green
    pca.channels[1].duty_cycle = brightness #Red  
    pca.channels[2].duty_cycle = 0x0000        

    pca.channels[3].duty_cycle = brightness #Green
    pca.channels[4].duty_cycle = 0x0000 #Red  
    pca.channels[5].duty_cycle = 0x0000            

    pca.channels[6].duty_cycle = 0x0000 #Green
    pca.channels[7].duty_cycle = brightness #Red
    pca.channels[12].duty_cycle = 0x0000        

    pca.channels[13].duty_cycle = brightness #Green
    pca.channels[14].duty_cycle = 0x0000 #Red
    pca.channels[15].duty_cycle = 0x0000        

    pca.channels[8].duty_cycle = 0x0000 #Test
    pca.channels[9].duty_cycle = 0x0000 #Test
    pca.channels[10].duty_cycle = 0x0000 #Test
    pca.channels[11].duty_cycle = 0x0000 #Test 

    time.sleep(2)

    pca.channels[0].duty_cycle = brightness #Green
    pca.channels[1].duty_cycle = 0x0000 #Red
    pca.channels[2].duty_cycle = 0x0000      

    pca.channels[3].duty_cycle = 0x0000 #Green
    pca.channels[4].duty_cycle = brightness #Red
    pca.channels[5].duty_cycle = 0x0000      

    pca.channels[6].duty_cycle = brightness #Green
    pca.channels[7].duty_cycle = 0x0000 #Red
    pca.channels[12].duty_cycle = 0x0000     

    pca.channels[13].duty_cycle = 0x0000 #Green
    pca.channels[14].duty_cycle = brightness #Red
    pca.channels[15].duty_cycle = 0x0000      

    pca.channels[8].duty_cycle = Test #Test
    pca.channels[9].duty_cycle = Test #Test
    pca.channels[10].duty_cycle = Test #Test
    pca.channels[11].duty_cycle = Test #Test 

    time.sleep(2)
