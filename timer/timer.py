#!/usr/bin/env python
__author__ = 'coleman'

import time
import os
import sys
import argparse

start_time = time.time()


def main(args):
    parser = argparse.ArgumentParser(description='timer from the command line', prog='timer')
    parser.add_argument('minutes', type=int)
    parser.add_argument('message', nargs='*', type=str)
    opts = parser.parse_args(args) # command line arguments
    startTimer(opts.minutes, opts.message)

def startTimer(minutes, message):

    message = ' '.join(message)
    os.system('notify-send \' '+ message +'\'')
    seconds = minutes * 60
    os.system('notify-send \'Starting ' + str(minutes) + ' minute timer\'')
    time.sleep(seconds)
    os.system('notify-send \'Timer is up\n '+ message +'\'')


def displayMessage(message):
    pass

#    message = ' '.join(message)
#    os.system('notify-send \' '+ message +'\'')
#    seconds = minutes * 60
#    os.system('notify-send \'Starting ' + str(minutes) + ' minute timer\'')
#    time.sleep(seconds)
#    os.system('notify-send \'Timer is up\n '+ message +'\'')


if __name__ == '__main__':    
    main(sys.argv[1:])

