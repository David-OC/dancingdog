#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import curses, time, locale, sys, os
import pygame
from doggunk import *

import signal
import sys

def signal_handler(signal, frame):
    curses.noqiflush()

scriptpath = os.path.dirname(os.path.abspath(__file__))
musicfile = "mus_dance_of_dog.ogg"

signal.signal(signal.SIGINT, signal_handler)
pygame.init()
pygame.mixer.music.load(scriptpath + '/' + musicfile)
pygame.mixer.music.play()

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

    while pygame.mixer.music.get_busy():
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
