#!/usr/bin/python3
# -*- coding:utf-8 -*-

import epd2in13
import time
from PIL import Image, ImageDraw, ImageFont
import requests
import threading

old_data = None
data = None
elip = 0
view = "main"
font15 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 15)
font12 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 12)
fields = ("field1", "field2", "field3", "field4", "field5", "field6", "field7", "field8")
views = ("main", "date", "clean")
fields_names = [None] * 8
fields_feeds = [None] * 8

def get_thingspeak_data():
    url = requests.get('https://api.thingspeak.com/channels/775759/feeds.json?results=1')
    j = url.json()
    return j


# WYSWIETLENIE INTERFEJSU NA EKRANIE:
epd = epd2in13.EPD()
epd.init(epd.lut_full_update)
epd.Clear(0xFF)
image = Image.new('1', (epd2in13.EPD_HEIGHT, epd2in13.EPD_WIDTH), 255)  # 255: clear the frame
draw = ImageDraw.Draw(image)

draw.text((0, 0), 'Time: ', font=font15, fill=0)
draw.text((0, 25), 'PM1.0: ', font=font15, fill=0)
draw.text((100, 25), 'ug/m3', font=font15, fill=0)
draw.text((0, 40), 'PM2.5: ', font=font15, fill=0)
draw.text((100, 40), 'ug/m3', font=font15, fill=0)
draw.text((0, 55), 'PM10: ', font=font15, fill=0)
draw.text((100, 55), 'ug/m3', font=font15, fill=0)

draw.text((0, 70), 'Temperature: ', font=font15, fill=0)
draw.text((180, 70), '*C', font=font15, fill=0)
draw.text((0, 85), 'Pressure: ', font=font15, fill=0)
draw.text((180, 85), 'hPa', font=font15, fill=0)
draw.text((0, 100), 'Humidity: ', font=font15, fill=0)
draw.text((180, 100), '%', font=font15, fill=0)

epd.display(epd.getbuffer(image))

# AKTUALIZACJA POL DANYCH INTERFEJSU:
epd.init(epd.lut_partial_update)

data = get_thingspeak_data()
time.sleep(1)

channel_id = data["channel"]["id"]
for i in range(8):
    fields_names[i] = data["channel"][fields[i]]
for i in range(8):
    fields_feeds[i] = data["feeds"][0][fields[i]]
created_at = data["feeds"][0]["created_at"]

draw.rectangle((60, 25, 100, 40), fill=255,)
draw.text((60, 25), str(fields_feeds[fields_names.index("PM1.0")]), font=font15, fill=0)
draw.rectangle((60, 40, 100, 55), fill=255,)
draw.text((60, 40), str(fields_feeds[fields_names.index("PM2.5")]), font=font15, fill=0)
draw.rectangle((60, 55, 100, 70), fill=255,)
draw.text((60, 55), str(fields_feeds[fields_names.index("PM10")]), font=font15, fill=0)

draw.rectangle((110, 70, 180, 85), fill=255,)
draw.text((110, 70), str(fields_feeds[fields_names.index("Temperature")]), font=font15, fill=0)
draw.rectangle((110, 85, 180, 100), fill=255,)
draw.text((110, 85), str(fields_feeds[fields_names.index("Pressure")]), font=font15, fill=0)
draw.rectangle((110, 100, 180, 115), fill=255,)
draw.text((110, 100), str(fields_feeds[fields_names.index("Humidity")]), font=font15, fill=0)

draw.rectangle((50, 0, 250, 15), fill=255, outline=0)
draw.text((50, 0), time.strftime('%d %b %Y %H:%M:%S'), font=font15, fill=0)

    # if elip == 0:
    #     draw.ellipse([0, 0, 8, 8], fill=255)
    #     draw.ellipse([10, 0, 18, 8], fill=255)
    #     draw.ellipse([20, 0, 28, 8], fill=255)
    #     draw.ellipse([30, 0, 38, 8], fill=255)
    #     elip = 1
    # elif elip == 1:
    #     draw.ellipse([0, 0, 8, 8], fill=0)
    #     elip = 2
    # elif elip == 2:
    #     draw.ellipse([10, 0, 18, 8], fill=0)
    #     elip = 3
    # elif elip == 3:
    #     draw.ellipse([20, 0, 28, 8], fill=0)
    #     elip = 4
    # elif elip == 4:
    #     draw.ellipse([30, 0, 38, 8], fill=0)
    #     elip = 0

epd.display(epd.getbuffer(image))
exit()