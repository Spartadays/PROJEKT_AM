#!/usr/bin/python3
# -*- coding:utf-8 -*-

import epd2in13
import time, sys
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont

font15 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 15)
font12 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 12)

# WYSWIETLENIE INTERFEJSU NA EKRANIE:
text = ""
if len(sys.argv) >= 2:
    text = sys.argv[1]

epd = epd2in13.EPD()
epd.init(epd.lut_full_update)
epd.Clear(0xFF)
image = Image.new('1', (epd2in13.EPD_HEIGHT, epd2in13.EPD_WIDTH), 255)  # 255: clear the frame
draw = ImageDraw.Draw(image)
draw.text((0, 0), 'Time: ', font=font15, fill=0)
draw.rectangle((50, 0, 250, 15), fill=255, outline=0)
draw.text((50, 0), time.strftime('%d %b %Y %H:%M:%S'), font=font15, fill=0)
draw.text((0, 30), "Your text:", font=font15, fill=0)
draw.text((0, 60), str(text), font=font15, fill=0)
epd.display(epd.getbuffer(image))
exit()