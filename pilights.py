# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# This simple test outputs a 50% duty cycle PWM single on the 0th channel. Connect an LED and
# resistor in series to the pin to visualize duty cycle changes and its impact on brightness.

from operator import truediv
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
LEDON = 0x1FFF  
HALF = 0x3bbb #LEDHALF
QRTR = 0x1ddd #LEDQUARTER brightness
        

def choose_mode():
        global time_conversion
        
        while True:
#            lighting_mode = random.randrange(6)
            lighting_mode = 5
            time_conversion = random.randrange(10,15)

            if lighting_mode == 0:
                print("Running simplefade for " + str(time_conversion) + " seconds.")
                simple_fade(time_conversion)
            elif lighting_mode == 1:
                print("Running stripkit for " + str(time_conversion) + " seconds.")
                strip_kit(time_conversion)
            elif lighting_mode == 2:
                print("Running stripkit_reid1 for " + str(time_conversion) + " seconds.")
                stripkit_reid1(time_conversion)
            elif lighting_mode == 3:
                print("Running rows for " + str(time_conversion) + " seconds.")
                rows(time_conversion)
            elif lighting_mode == 4:
                print("Running jingle_bells for " + str(time_conversion) + " seconds.")
                jingle_bells(time_conversion)
            elif lighting_mode == 5:
                print("Running stvaltrix " + str(time_conversion) + " seconds.")
                stvaltrix(time_conversion)

            print("Restarting current_mode")

def simple_fade(time_in_seconds):
    start_time=time.time()
    TIMETOQUIT = False
    
    color_fade = LEDON 
    fade_increment = 100
    channel_number = 0

    while not TIMETOQUIT:
        while color_fade > -1 :
            channel_number=random.randrange(16)
#            print("Channel " + str(channel_number) + " is set to " + str(color_fade) )
            pca.channels[channel_number].duty_cycle = color_fade
            color_fade = color_fade - fade_increment
        pca.channels[channel_number].duty_cycle = 0x0000
    
        color_fade = 0 #Bounds Check
    
        while color_fade <= LEDON :
            channel_number=random.randrange(16)
#            print("Channel " + str(channel_number) + " is set to " + str(color_fade) )
            pca.channels[channel_number].duty_cycle = color_fade
            color_fade = color_fade + fade_increment
        color_fade = LEDON #Bounds Check

        current_time=time.time()
 #       print("Current time is " + str(current_time))
        if (current_time - start_time) > time_in_seconds:
            TIMETOQUIT = True 
    
    return


def strip_kit(time_in_seconds): 
    start_time=time.time()
    wait = 1/32
    TIMETOQUIT = False
    while not TIMETOQUIT:
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

            current_time=time.time()
#            print("Current time is " + str(current_time))
            if (current_time - start_time) > time_in_seconds:
                TIMETOQUIT = True 
    return
                    
def stripkit_reid1(time_in_seconds):
    start_time=time.time()
    wait = 1/64 
    TIMETOQUIT = False
    while not TIMETOQUIT:
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

            current_time=time.time()
#            print("Current time is " + str(current_time))
            if (current_time - start_time) > time_in_seconds:
                TIMETOQUIT = True 
                
    return

def rows(time_in_seconds):
    start_time=time.time()
    wait = 1/8
    LEDMODE = LEDOFF
    TIMETOTURNONLEDS = False

    TIMETOQUIT = False 
    while not TIMETOQUIT:
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

        current_time=time.time()
#        print("Current time is " + str(current_time))
        if (current_time - start_time) > time_in_seconds:
            TIMETOQUIT = True 

    return

def jingle_bells(time_in_seconds):
    start_time=time.time()
    wait = 2 
    TIMETOQUIT = False
    
    low = 0x3FFF #Low 16383
    med = 0x7FFF #Medium 32767
    hi = 0xFFFF #High 65535

    brightness =  low
    Test = low


    while not TIMETOQUIT:
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

        time.sleep(wait)

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

        time.sleep(wait)

        current_time=time.time()
#        print("Current time is " + str(current_time))
        if (current_time - start_time) > time_in_seconds:
            TIMETOQUIT = True 

    return

def stvaltrix(time_in_seconds):
    start_time=time.time()
    TIMETOQUIT = False

    while not TIMETOQUIT:
    
 #   LEDON = 0x7777
 #   LEDOFF = 0x000
 #   HALF = 0x3bbb
#    QRTR = 0x1ddd

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
        pca.channels[0].duty_cycle = QRTR #Green
        pca.channels[1].duty_cycle = LEDOFF #Red
        pca.channels[2].duty_cycle = LEDOFF #Blue
        time.sleep(wait)
        pca.channels[3].duty_cycle = LEDOFF #Green
        pca.channels[4].duty_cycle = LEDMODE #Red
        pca.channels[5].duty_cycle = LEDMODE #Blue
        time.sleep(onwait) #off
        pca.channels[3].duty_cycle = QRTR #Green
        pca.channels[4].duty_cycle = LEDOFF #Red
        pca.channels[5].duty_cycle = LEDOFF #Blue
        time.sleep(wait)
        pca.channels[6].duty_cycle = LEDOFF #Green
        pca.channels[7].duty_cycle = LEDMODE #Red
        pca.channels[12].duty_cycle = LEDMODE #Blue 
        time.sleep(onwait) #off
        pca.channels[6].duty_cycle = QRTR #Green
        pca.channels[7].duty_cycle = LEDOFF #Red
        pca.channels[12].duty_cycle = LEDOFF #Blue 
        time.sleep(wait)
        pca.channels[13].duty_cycle = LEDOFF #Green
        pca.channels[14].duty_cycle = LEDMODE #Red
        pca.channels[15].duty_cycle = LEDMODE #Blue
        time.sleep(onwait) #off
        pca.channels[13].duty_cycle = QRTR #Green
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
        pca.channels[6].duty_cycle = QRTR #Green
        time.sleep(wait)
        pca.channels[5].duty_cycle = LEDMODE #Blue
        pca.channels[4].duty_cycle = LEDMODE #Red
        pca.channels[3].duty_cycle = LEDOFF #Green 
        time.sleep(onwait)
        pca.channels[5].duty_cycle = LEDOFF #Blue
        pca.channels[4].duty_cycle = LEDOFF #Red
        pca.channels[3].duty_cycle = QRTR #Green 
        time.sleep(wait)
        pca.channels[2].duty_cycle = LEDMODE #Blue
        pca.channels[1].duty_cycle = LEDMODE #Red
        pca.channels[0].duty_cycle = LEDOFF #Green
    #    time.sleep(onwait)
        pca.channels[2].duty_cycle = LEDOFF #Blue
        pca.channels[1].duty_cycle = LEDOFF #Red
        pca.channels[0].duty_cycle = QRTR #Green

    #    if TIMETOTURNONLEDS:
    #        TIMETOTURNONLEDS = False
    #    elif not TIMETOTURNONLEDS:
    #        TIMETOTURNONLEDS = True

    current_time=time.time()
        print("Current time is " + str(current_time))
        if (current_time - start_time) > time_in_seconds:
            TIMETOQUIT = True 

   return

#def new_mode(time_in_seconds)
#    start_time=time.time()
#    TIMETOQUIT = False
#
#    while not TIMETOQUIT:
#       new mode goes here
#        ...
#        ...
#        current_time=time.time()
#        print("Current time is " + str(current_time))
#        if (current_time - start_time) > time_in_seconds:
#            TIMETOQUIT = True 
#   return

def main():
    choose_mode()

if __name__ == "__main__":
    main()
