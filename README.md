# pilights
Control RGB LED light strips with a PCA9685 controller and a Raspberry Pi.

This project is comprised of a raspberry pi zero w connected to a PCA9685 16-Channel 12-bit PWM/Servo Driver - I2C interface. In order to handle the current requirements of the LED strips a transister is required on the output from the PCA9685. The controller assembly outputs 12 channels from the PCA9685 for the RGB LED light strips, with 4 channels  (8, 9, 10, and 11) going to LEDs on the controller board for testing purposes.
