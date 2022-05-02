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
LEDMODE = LEDOFF
TIMETOTURNONLEDS = True
while True:
    wait = 1/8 

    if TIMETOTURNONLEDS: 
        LEDMODE = LEDON
    elif not TIMETOTURNONLEDS:
        LEDMODE = LEDOFF

    pca.channels[0].duty_cycle = LEDMODE #Red
    pca.channels[1].duty_cycle = LEDMODE #Blue
    pca.channels[2].duty_cycle = LEDMODE #Green
    time.sleep(wait)
    pca.channels[3].duty_cycle = LEDMODE #Red
    pca.channels[4].duty_cycle = LEDMODE #Blue
    pca.channels[5].duty_cycle = LEDMODE #Green
    time.sleep(wait)
    pca.channels[6].duty_cycle = LEDMODE #Red
    pca.channels[7].duty_cycle = LEDMODE #Blue
    pca.channels[12].duty_cycle = LEDMODE #Green
    time.sleep(wait)
    pca.channels[13].duty_cycle = LEDMODE #Red
    pca.channels[14].duty_cycle = LEDMODE #Blue
    pca.channels[15].duty_cycle = LEDMODE #Green

    if TIMETOTURNONLEDS:
        TIMETOTURNONLEDS = False
    elif not TIMETOTURNONLEDS:
        TIMETOTURNONLEDS = True
