# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# This simple test outputs a 50% duty cycle PWM single on the 0th channel. Connect an LED and
# resistor in series to the pin to visualize duty cycle changes and its impact on brightness.

from board import SCL, SDA
import busio
import time
import board
import pwmio

# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685

import random 

# Create the I2C bus interface.
i2c_bus = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c_bus)

# Set the PWM frequency to 60hz.
pca.frequency = 60

# Set the PWM duty cycle for channel zero to 50%. duty_cycle is 16 bits to match other PWM objects
# but the PCA9685 will only actually give 12 bits of resolution.
#MODDED BY RON


# ropertyduty_cycle: int
# 16 bit value that dictates how much of one cycle is high (1) versus low (0). 
# 0xffff will always be high, 0 will always be low and 0x7fff will be half high and then half low.

color_fade = 0xFFFF
fade_increment = 100
channel_number = 0

#while channel_number <= 16 :   
#    pca.channels[channel_number].duty_cycle = 0x0000
#    channel_number = channel_number + 1

while True:
    while color_fade > -1 :
        channel_number=random.randrange(16)
        print("Channel " + str(channel_number) + " is set to " + str(color_fade) )
        pca.channels[channel_number].duty_cycle = color_fade
        color_fade = color_fade - fade_increment
    pca.channels[channel_number].duty_cycle = 0x0000


    color_fade = 0 #Bounds Check

    while color_fade <= 0xFFFF :
        channel_number=random.randrange(16)
        print("Channel " + str(channel_number) + " is set to " + str(color_fade) )
        pca.channels[channel_number].duty_cycle = color_fade
        color_fade = color_fade + fade_increment

    color_fade = 0xFFFF #Bounds Check
