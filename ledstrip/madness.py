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

while True:
    pca.channels[0].duty_cycle = 0xFFFF # Red
    pca.channels[1].duty_cycle = 0xFFFF # Blue
    pca.channels[2].duty_cycle = 0xFFFF # Green
    time.sleep(1)
    pca.channels[0].duty_cycle = 0x0000
    pca.channels[1].duty_cycle = 0x0000
    pca.channels[2].duty_cycle = 0x0000
    time.sleep(1)


#led = pwmio.PWMOut(board.D5, frequency=5000, duty_cycle=0)
#led = pwmio.PWMOut(pca.channels[0], frequency=5000,duty_cycle=0)
#while True:
#        for i in range(100):
#            # PWM LED up and down
#            if i < 50:
#                led.duty_cycle = int(i * 2 * 65535 / 100)  # Up
#            else:
#                led.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
#            time.sleep(0.01)
