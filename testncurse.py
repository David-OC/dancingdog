#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import curses, time, locale, sys, traceback
#import time
#import locale
#import sys
from dogspritetext import *
try:
    locale.setlocale(locale.LC_ALL, '')
    # Create curses screen
    scr = curses.initscr()
    #scr.refresh()
    curses.noecho()

    # Get screen width/height
    #height,width = scr.getmaxyx()

    # Fill the window with text (note that 5 lines are lost forever)
#for i in range(0, height + 15):
#    mypad.addstr("{0} This is a sample string...\n".format(i))
#    if i > height: mypad_pos = min(i - height, mypad_height - height)
#    mypad_refresh()
#    time.sleep(0.05)
#
    while True:
        scr.addstr(0,0,dogdance1)
        scr.refresh()
        time.sleep(0.5)
        scr.addstr(0,0,dogdance2)
        scr.refresh()
        time.sleep(0.5)

# End curses
#curses.nocbreak()
    curses.echo()
    curses.endwin()
except:
    #curses.nocbreak()
    exec_info = sys.exc_info()
    traceback.print_exception(*exec_info)
    del exec_info
finally:
    curses.echo()
    curses.nocbreak()
    curses.endwin()
