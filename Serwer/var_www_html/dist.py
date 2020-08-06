#!/usr/bin/python3
# -*- coding:utf-8 -*-

import time, sys
import RPi.GPIO as GPIO


def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start_time = time.time()
    stop_time = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        stop_time = time.time()
    time_elapsed = stop_time - start_time
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    dis = (time_elapsed * 34300) / 2
    return dis


# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 27

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

rang = 500
if len(sys.argv) >= 2:
    rang = int(sys.argv[1])

dist = distance()
dist_int = int(dist)

if dist_int > rang:
    dist_int = rang

print(dist_int)

sys.exit(0)