import busio
from board import SCL, SDA

# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685

i2c_bus = busio.I2C(SCL, SDA)

# Set the PWM frequency to 60hz.
pca = PCA9685(i2c_bus)

# Set the PWM frequency to 60hz
pca.frequency = 60

class HardwareStrategy:
    def __init__(self):
        print("hardware strategy has been initialized")

    def duty_cycle(self, channel, value):
        pca.channels[channel].duty_cycle = value
