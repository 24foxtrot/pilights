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

#simple_fade() = 0
#strip_kit() = 1

def choose_mode():
    global time_conversion

    while True:
        lighting_mode = random.randrange(1)
        lighting_time = random.randrange(3,6)
        time_conversion = lighting_time/3

        print("The current mode is " + str(lighting_mode) + " for " + str(lighting_time) + " minutes.")
        time.sleep(time_conversion)

        if lighting_mode == 0 :
            simple_fade()
        return
        elif lighting_mode == 1:
            stripkit()
        return
        else
        print("Your program sucks.")
color_fade = 0xFFFF
fade_increment = 100
channel_number = 0


def simple_fade():
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
        return

def strip_kit():
    wait = 1/128

    LEDSTRIP0 = 0, 1, 2
    LEDSTRIP1 = 3, 4, 5
    LEDSTRIP2 = 6, 7, 12
    LEDSTRIP3 = 13, 14, 15
    stripkit = 0, 3, 6, 13, 1, 4, 7, 14, 2, 5, 12, 15

    #Are the LEDs on when they should be off? If So Change this to FALSE. ELSE TRUE
    NORMALED = 0

    if NORMALED == 1:
       LEDOFF = 0x000
       LEDON = 0x7FFF
    else:
       LEDOFF = 0x7FFF
       LEDON = 0x000

    while True:
        for x in stripkit:
            pca.channels[x].duty_cycle = LEDON
            pca.channels[x].duty_cycle = LEDOFF
            pca.channels[x].duty_cycle = LEDOFF
            pca.channels[x].duty_cycle = LEDOFF
            time.sleep(wait)
            pca.channels[x].duty_cycle = LEDOFF
            pca.channels[x].duty_cycle = LEDON
            pca.channels[x].duty_cycle = LEDOFF
            pca.channels[x].duty_cycle = LEDOFF
            time.sleep(wait)
            pca.channels[x].duty_cycle = LEDOFF
            pca.channels[x].duty_cycle = LEDOFF
            pca.channels[x].duty_cycle = LEDON
            pca.channels[x].duty_cycle = LEDOFF
            time.sleep(wait)
            pca.channels[x].duty_cycle = LEDOFF
            pca.channels[x].duty_cycle = LEDOFF
            pca.channels[x].duty_cycle = LEDOFF
            pca.channels[x].duty_cycle = LEDON
            time.sleep(wait)
            return
