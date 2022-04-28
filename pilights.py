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

# ropertyduty_cycle: int
# 16 bit value that dictates how much of one cycle is high (1) versus low (0). 
# 0xffff will always be high, 0 will always be low and 0x7fff will be half high and then half low.


LEDSTRIP0 = 0, 1, 2
LEDSTRIP1 = 3, 4, 5
LEDSTRIP2 = 6, 7, 12
LEDSTRIP3 = 13, 14, 15
stripkit = 0, 3, 6, 13, 1, 4, 7, 14, 2, 5, 12, 15
testleds = 8, 9 , 10, 11
LEDOFF = 0x000
LEDON = 0xFFFF

def choose_mode():
        global time_conversion
        lighting_time = 0
        
        while True:
#            lighting_mode = random.randrange(3)
#            lighting_time = random.randrange(3,6) 
            lighting_mode = 2 
#            time_conversion = lighting_time/30
            time_conversion = random.randrange(10,15)
#            print("The current mode is " + str(lighting_mode) + " for " + str(lighting_time) + " minutes.") 

            if lighting_mode == 1:
                print("Running simplefade")
                simple_fade()
            elif lighting_mode == 1:
                print("Running stripkit")
                strip_kit()
            elif lighting_mode == 2:
                print("Running stripkit_reid1")
                stripkit_reid1()
            time.sleep(time_conversion)
            print("for " + str(time_conversion) + " seconds.")
choose_mode

def simple_fade(): #Works I think?

    color_fade = 0xFFFF
    fade_increment = 100
    channel_number = 0

    while True:
        while color_fade > -1 :
            channel_number=random.randrange(16)
#            print("Channel " + str(channel_number) + " is set to " + str(color_fade) )
            pca.channels[channel_number].duty_cycle = color_fade
            color_fade = color_fade - fade_increment
        pca.channels[channel_number].duty_cycle = 0x0000
    
        color_fade = 0 #Bounds Check
    
        while color_fade <= 0xFFFF :
            channel_number=random.randrange(16)
#            print("Channel " + str(channel_number) + " is set to " + str(color_fade) )
            pca.channels[channel_number].duty_cycle = color_fade
            color_fade = color_fade + fade_increment
        color_fade = 0xFFFF #Bounds Check
    #return
        choose_mode()

def strip_kit():  #works don't touch
    wait = 1/32

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
        choose_mode() 
                    
def stripkit_reid1():
    wait = 1/64 
#    while True:
    while time_conversion > 0:
        for x in LEDSTRIP0:
            #Forward
            pca.channels[x].duty_cycle = LEDON
            pca.channels[x].duty_cycle = LEDOFF
            pca.channels[x].duty_cycle = LEDOFF
            pca.channels[x].duty_cycle = LEDOFF
            pca.channels[x+3].duty_cycle = LEDON
            pca.channels[x+3].duty_cycle = LEDOFF
            pca.channels[x+3].duty_cycle = LEDOFF
            pca.channels[x+3].duty_cycle = LEDOFF
            pca.channels[x+6].duty_cycle = LEDON
            pca.channels[x+6].duty_cycle = LEDOFF
            pca.channels[x+6].duty_cycle = LEDOFF
            pca.channels[x+6].duty_cycle = LEDOFF
            pca.channels[x+13].duty_cycle = LEDON
            pca.channels[x+13].duty_cycle = LEDOFF
            pca.channels[x+13].duty_cycle = LEDOFF
            pca.channels[x+13].duty_cycle = LEDOFF
            time.sleep(wait)
            pca.channels[x].duty_cycle = LEDOFF
            pca.channels[x].duty_cycle = LEDON
            pca.channels[x].duty_cycle = LEDOFF
            pca.channels[x].duty_cycle = LEDOFF
            pca.channels[x+6].duty_cycle = LEDOFF
            pca.channels[x+6].duty_cycle = LEDON
            pca.channels[x+6].duty_cycle = LEDOFF
            pca.channels[x+6].duty_cycle = LEDOFF
            pca.channels[x+3].duty_cycle = LEDOFF
            pca.channels[x+3].duty_cycle = LEDON
            pca.channels[x+3].duty_cycle = LEDOFF
            pca.channels[x+3].duty_cycle = LEDOFF
            pca.channels[x+13].duty_cycle = LEDOFF
            pca.channels[x+13].duty_cycle = LEDON
            pca.channels[x+13].duty_cycle = LEDOFF
            pca.channels[x+13].duty_cycle = LEDOFF
            time.sleep(wait)
            pca.channels[x].duty_cycle = LEDOFF
            pca.channels[x].duty_cycle = LEDOFF
            pca.channels[x].duty_cycle = LEDON
            pca.channels[x].duty_cycle = LEDOFF
            pca.channels[x+3].duty_cycle = LEDOFF
            pca.channels[x+3].duty_cycle = LEDOFF
            pca.channels[x+3].duty_cycle = LEDON
            pca.channels[x+3].duty_cycle = LEDOFF
            pca.channels[x+6].duty_cycle = LEDOFF
            pca.channels[x+6].duty_cycle = LEDOFF
            pca.channels[x+6].duty_cycle = LEDON
            pca.channels[x+6].duty_cycle = LEDOFF
            pca.channels[x+13].duty_cycle = LEDOFF
            pca.channels[x+13].duty_cycle = LEDOFF
            pca.channels[x+13].duty_cycle = LEDON
            pca.channels[x+13].duty_cycle = LEDOFF
            time.sleep(wait)
            pca.channels[x].duty_cycle = LEDOFF
            pca.channels[x].duty_cycle = LEDOFF
            pca.channels[x].duty_cycle = LEDOFF
            pca.channels[x].duty_cycle = LEDON
            pca.channels[x+3].duty_cycle = LEDOFF
            pca.channels[x+3].duty_cycle = LEDOFF
            pca.channels[x+3].duty_cycle = LEDOFF
            pca.channels[x+3].duty_cycle = LEDON
            pca.channels[x+6].duty_cycle = LEDOFF
            pca.channels[x+6].duty_cycle = LEDOFF
            pca.channels[x+6].duty_cycle = LEDOFF
            pca.channels[x+6].duty_cycle = LEDON
            pca.channels[x+13].duty_cycle = LEDOFF
            pca.channels[x+13].duty_cycle = LEDOFF
            pca.channels[x+13].duty_cycle = LEDOFF
            pca.channels[x+13].duty_cycle = LEDON
            time.sleep(wait)
choose_mode()
