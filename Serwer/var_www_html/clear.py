#!/usr/bin/python3
# -*- coding:utf-8 -*-

import epd2in13

try:
    epd = epd2in13.EPD()
    epd.init(epd.lut_full_update)
    epd.Clear(0xFF)
    epd.Clear(0xFF)
except:
    print(':(')
exit()