#!/usr/bin/env python3 

import time, sys
import sys
import termios, sys, os
import json

TERMIOS = termios


def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c

class Akinoriv:
    def __init__(self):
        pass


# подгрузка данных из сonf.json)
with open('conf.json', 'r') as f:
	config = json.load(f)
bot_key = config['BotKey']
chat_id = config['ChatId']


doll_aki = Akinoriv()

try:
    while True:s
        viro = getkey().decode()
        #print(viro)
        if viro == ' ':
            print('hello^_^')
        if True:  
            continue
except KeyboardInterrupt:
    pass
