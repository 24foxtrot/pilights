from strategy.console import ConsoleStrategy
'''
    Example:
        from the root of the repo run the following:
        python -m examples.console_example
'''

import time
import random

def choose_mode():
        global time_conversion

        while True:
            time_conversion = random.randrange(10,15)

            print("Running jingle_bells for " + str(time_conversion) + " seconds.")
            jingle_bells(time_conversion)

            print("Restarting current_mode")

pca = ConsoleStrategy()

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
        pca.duty_cycle(0, 0x0000) #Green
        pca.duty_cycle(1, brightness) #Red
        pca.duty_cycle(2, 0x0000)

        pca.duty_cycle(3, brightness) #Green
        pca.duty_cycle(4, 0x0000) #Red
        pca.duty_cycle(5, 0x0000)

        pca.duty_cycle(6, 0x0000) #Green
        pca.duty_cycle(7, brightness) #Red
        pca.duty_cycle(12, 0x0000)

        pca.duty_cycle(13, brightness) #Green
        pca.duty_cycle(14, 0x0000) #Red
        pca.duty_cycle(15, 0x0000)

        pca.duty_cycle(8, 0x0000) #Test
        pca.duty_cycle(9, 0x0000) #Test
        pca.duty_cycle(10, 0x0000) #Test
        pca.duty_cycle(11, 0x0000) #Test

        time.sleep(wait)

        pca.duty_cycle(0, brightness) #Green
        pca.duty_cycle(1, 0x0000) #Red
        pca.duty_cycle(2, 0x0000)

        pca.duty_cycle(3, 0x0000) #Green
        pca.duty_cycle(4, brightness) #Red
        pca.duty_cycle(5, 0x0000)

        pca.duty_cycle(6, brightness) #Green
        pca.duty_cycle(7, 0x0000) #Red
        pca.duty_cycle(12, 0x0000)

        pca.duty_cycle(13, 0x0000) #Green
        pca.duty_cycle(14, brightness) #Red
        pca.duty_cycle(15, 0x0000)

        pca.duty_cycle(8, Test) #Test
        pca.duty_cycle(9, Test) #Test
        pca.duty_cycle(10, Test) #Test
        pca.duty_cycle(11, Test) #Test

        time.sleep(wait)

        current_time=time.time()

        if (current_time - start_time) > time_in_seconds:
            TIMETOQUIT = True
    return

def main():
    choose_mode()

main()