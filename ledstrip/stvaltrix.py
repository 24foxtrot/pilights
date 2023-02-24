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

# Set the PWM duty cycle for channel zero to 50%. duty_cycle is 16 bits to match other PWM objects
# but the PCA9685 will only actually give 12 bits of resolution.
#MODDED BY RON

LEDON = 0x7777
LEDOFF = 0x000
HALF = 0x3bbb
QRTR = 0x1ddd

ONLVL = LEDON
LEDMODE = LEDOFF
TIMETOTURNONLEDS = True

while True:
    wait = .0625 #(1/8)/2 
    onwait = .25  #.1666 #(1/3)/2

    if TIMETOTURNONLEDS: 
        LEDMODE = LEDON
    elif not TIMETOTURNONLEDS:
        LEDMODE = LEDOFF

    pca.channels[0].duty_cycle = LEDOFF #Green
    pca.channels[1].duty_cycle = LEDMODE #Red
    pca.channels[2].duty_cycle = LEDMODE #Blue
    time.sleep(onwait) #off 
    pca.channels[0].duty_cycle = ONLVL #Green
    pca.channels[1].duty_cycle = LEDOFF #Red
    pca.channels[2].duty_cycle = LEDOFF #Blue
    time.sleep(wait)
    pca.channels[3].duty_cycle = LEDOFF #Green
    pca.channels[4].duty_cycle = LEDMODE #Red
    pca.channels[5].duty_cycle = LEDMODE #Blue
    time.sleep(onwait) #off
    pca.channels[3].duty_cycle = ONLVL #Green
    pca.channels[4].duty_cycle = LEDOFF #Red
    pca.channels[5].duty_cycle = LEDOFF #Blue
    time.sleep(wait)
    pca.channels[6].duty_cycle = LEDOFF #Green
    pca.channels[7].duty_cycle = LEDMODE #Red
    pca.channels[12].duty_cycle = LEDMODE #Blue 
    time.sleep(onwait) #off
    pca.channels[6].duty_cycle = ONLVL #Green
    pca.channels[7].duty_cycle = LEDOFF #Red
    pca.channels[12].duty_cycle = LEDOFF #Blue 
    time.sleep(wait)
    pca.channels[13].duty_cycle = LEDOFF #Green
    pca.channels[14].duty_cycle = LEDMODE #Red
    pca.channels[15].duty_cycle = LEDMODE #Blue
    time.sleep(onwait) #off
    pca.channels[13].duty_cycle = ONLVL #Green
    pca.channels[14].duty_cycle = LEDOFF #Red
    pca.channels[15].duty_cycle = LEDOFF #Blue
#Reverse
    time.sleep(wait) #REVERSE --Reverse all LEDMODES due to TIMETOTURNONLEDS flipflip breaking colors. 
    pca.channels[12].duty_cycle = LEDMODE #Blue
    pca.channels[7].duty_cycle = LEDMODE #Red
    pca.channels[6].duty_cycle = LEDOFF #Green
    time.sleep(onwait)
    pca.channels[12].duty_cycle = LEDOFF #Blue
    pca.channels[7].duty_cycle = LEDOFF #Red
    pca.channels[6].duty_cycle = ONLVL #Green
    time.sleep(wait)
    pca.channels[5].duty_cycle = LEDMODE #Blue
    pca.channels[4].duty_cycle = LEDMODE #Red
    pca.channels[3].duty_cycle = LEDOFF #Green 
    time.sleep(onwait)
    pca.channels[5].duty_cycle = LEDOFF #Blue
    pca.channels[4].duty_cycle = LEDOFF #Red
    pca.channels[3].duty_cycle = ONLVL #Green 
    time.sleep(wait)
    pca.channels[2].duty_cycle = LEDMODE #Blue
    pca.channels[1].duty_cycle = LEDMODE #Red
    pca.channels[0].duty_cycle = LEDOFF #Green
#    time.sleep(onwait)
    pca.channels[2].duty_cycle = LEDOFF #Blue
    pca.channels[1].duty_cycle = LEDOFF #Red
    pca.channels[0].duty_cycle = ONLVL #Green

#    if TIMETOTURNONLEDS:
#        TIMETOTURNONLEDS = False
#    elif not TIMETOTURNONLEDS:
#        TIMETOTURNONLEDS = True

def main():
    if __name__--"__main__":
        main()
