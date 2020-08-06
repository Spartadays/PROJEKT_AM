#!/usr/bin/python3
# -*- coding:utf-8 -*-

import epd2in13
import time, sys
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont


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

font15 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 15)
font12 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 12)

# WYSWIETLENIE INTERFEJSU NA EKRANIE:
rang = 500
if len(sys.argv) >= 2:
    rang = int(sys.argv[1])

epd = epd2in13.EPD()
epd.init(epd.lut_full_update)
epd.Clear(0xFF)
image = Image.new('1', (epd2in13.EPD_HEIGHT, epd2in13.EPD_WIDTH), 255)  # 255: clear the frame
draw = ImageDraw.Draw(image)
draw.text((0, 0), 'Time: ', font=font15, fill=0)
draw.text((0, 60), '0', font=font15, fill=0)
draw.text((220, 60), str(rang), font=font15, fill=0)
draw.text((0, 80), 'Distance: ', font=font15, fill=0)

# AKTUALIZACJA POL DANYCH INTERFEJSU:
dist = distance()
draw.rectangle((100, 80, 200, 95), fill=255, outline=0)
draw.text((100, 80), ("%.2f cm" % dist), font=font15, fill=0)
if 500 < dist < 3000:
    dist = 500
elif dist > 3000:
    dist = 0
elif dist < 0:
    dist = 0
scaled_dist = dist*250/rang
draw.rectangle((50, 0, 250, 15), fill=255, outline=0)
draw.text((50, 0), time.strftime('%d %b %Y %H:%M:%S'), font=font15, fill=0)
draw.rectangle((0, 50, scaled_dist, 60), fill=0, outline=0)
draw.rectangle((scaled_dist, 50, 250, 60), fill=255, outline=0)
epd.display(epd.getbuffer(image))
flag = False
print("%.2f" % dist)
exit()