# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# This simple test outputs a 50% duty cycle PWM single on the 0th channel. Connect an LED and
# resistor in series to the pin to visualize duty cycle changes and its impact on brightness.

from board import SCL, SDA
import busio

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
pca.channels[0].duty_cycle = 0xFFFF #Red
pca.channels[1].duty_cycle = 0xFFFF #Blue
pca.channels[2].duty_cycle = 0xFFFF #Green

pca.channels[3].duty_cycle = 0x7FFF #Red
pca.channels[4].duty_cycle = 0x7FFF #Blue
pca.channels[5].duty_cycle = 0x7FFF #Green

pca.channels[6].duty_cycle = 0x3FFF #Red
pca.channels[7].duty_cycle = 0x3FFF #Blue
pca.channels[12].duty_cycle = 0x3FFF #Green

pca.channels[13].duty_cycle = 0x1FFF #Red
pca.channels[14].duty_cycle = 0x1FFF #Blue
pca.channels[15].duty_cycle = 0x1FFF #Green
