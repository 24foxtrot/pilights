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

#Modded by Ron
# 0x7FFF = ON
# 0XFFFF = off 

wait = 1/64

LEDSTRIP0 = 0, 1, 2  
LEDSTRIP1 = 3, 4, 5
LEDSTRIP2 = 6, 7, 12
LEDSTRIP3 = 13, 14, 15
stripkit = 0, 3, 6, 13, 1, 4, 7, 14, 2, 5, 12, 15
testleds = 8, 9 , 10, 11 

#Are the LEDs on when they should be off? If So Change this to FALSE. ELSE TRUE
NORMALED = 0 

if NORMALED == 1:
    LEDOFF = 0x000
    LEDON = 0x7FFF
else:
    LEDOFF = 0x7FFF
    LEDON = 0x000

while True:
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
