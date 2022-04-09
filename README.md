# pilights
Control RGB LED light strips with a PCA9685 controller and a Raspberry Pi.

This project is comprised of a raspberry pi zero w connected to a PCA9685 16-Channel 12-bit PWM/Servo Driver - I2C interface. In order to handle the current requirements of the LED strips a transister is required on the output from the PCA9685. The controller assembly outputs 12 channels from the PCA9685 for the RGB LED light strips, with and additional 4 channels  (8, 9, 10, and 11) going to LEDs on the controller board for testing purposes.

pilights.py - This is currently the primary file. 
It is supposed to pick a random operating mode and run that mode for between 3 and 5 minutes. 
Eventually we will try to make it work with RED ALERT, YELLOW ALERT, etc, from external games.
