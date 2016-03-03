#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import curses, time, locale, sys, traceback
from doggunk import *

try:
    locale.setlocale(locale.LC_ALL, '')
    scr = curses.initscr()
    
    curses.start_color()
    curses.use_default_colors()
    curses.curs_set(0)
    curses.noecho()

    curses.init_pair(1, 16, -1)
    curses.init_pair(2, 16, 255)
    curses.init_pair(3, 255, 16)
    curses.init_pair(4, -1, 16)
    
    height,width = scr.getmaxyx()
    
    posx = width / 2 - 9
    posy = height / 2 - 3

    while True:
        draw_dog1(scr,posx,posy)
        scr.refresh()
        time.sleep(0.2)

        draw_dog2(scr,posx,posy)
        scr.refresh()
        time.sleep(0.2)

    scr.keypad(0)
finally:
    curses.echo()
    curses.nocbreak()
    curses.endwin()
