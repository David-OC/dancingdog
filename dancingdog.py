# -*- coding: utf-8 -*-

import curses, time, locale, sys, os
import pygame
from pygame import mixer
import pyglet
from doggunk import *

import signal
import sys

def signal_handler(signal, frame):
    curses.noqiflush()

def signal_handler(signal, frame):
    pass    

def init_curses(scr):
    #Drawing the dog requires 256 colors, so this is done first
    curses.start_color()
    curses.use_default_colors()
    curses.curs_set(0)
    curses.noecho()
    #Setting up the color pairs for drawing the dog
    curses.init_pair(1, 16, -1)
    curses.init_pair(2, 16, 255)
    curses.init_pair(3, 255, 16)
    curses.init_pair(4, -1, 16)

#Get the path of the script and provide the name of the
# sound file.
scriptpath = os.path.dirname(os.path.abspath(__file__))
musicfile = "mus_dance_of_dog.ogg"

#Setting up signal handlers
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTSTP, signal_handler)

#Setting up pygame's audio parts
#pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(scriptpath + '/' + musicfile)
pygame.mixer.music.play()

#Perform the dog dance
try:
    locale.setlocale(locale.LC_ALL, '')
    scr = curses.initscr()
    
    init_curses(scr)
    
    height,width = scr.getmaxyx()

    posx = width / 2 - 9
    posy = height / 2 - 3

    #Keep the dogdance as long as the music plays
    while pygame.mixer.music.get_busy():
        draw_dog1(scr,posx,posy)
        scr.refresh()
        time.sleep(0.2)
        #Draw the next frame
        draw_dog2(scr,posx,posy)
        scr.refresh()
        time.sleep(0.2)
        #Repeat 'till the song stops

    scr.keypad(0)
finally:
#Clean up
    curses.echo()
    curses.nocbreak()
    curses.endwin()
