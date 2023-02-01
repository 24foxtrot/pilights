# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# This simple test outputs a 50% duty cycle PWM single on the 0th channel. Connect an LED and
# resistor in series to the pin to visualize duty cycle changes and its impact on brightness.

from board import SCL, SDA
from gpiozero import MotionSensor

import busio
import time

# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685

pir = MotionSensor(17)

# Create the I2C bus interface.
i2c_bus = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c_bus)

# Set the PWM frequency to 60hz.
pca.frequency = 60

while True:
    for x in [8, 9, 10, 11]:
        pca.channels[x].duty_cycle = 0x7FFF
        pca.channels[x].duty_cycle = 0xFFFF
        pca.channels[x].duty_cycle = 0xFFFF
        pca.channels[x].duty_cycle = 0xFFFF
        time.sleep(.0625)
        pca.channels[x].duty_cycle = 0xFFFF
        pca.channels[x].duty_cycle = 0x7FFF
        pca.channels[x].duty_cycle = 0xFFFF
        pca.channels[x].duty_cycle = 0xFFFF
        time.sleep(.0625)
        pca.channels[x].duty_cycle = 0xFFFF
        pca.channels[x].duty_cycle = 0xFFFF
        pca.channels[x].duty_cycle = 0x7FFF
        pca.channels[x].duty_cycle = 0xFFFF
        time.sleep(.0625)
        pca.channels[x].duty_cycle = 0xFFFF
        pca.channels[x].duty_cycle = 0xFFFF
        pca.channels[x].duty_cycle = 0xFFFF
        pca.channels[x].duty_cycle = 0x7FFF
        time.sleep(.0625)
