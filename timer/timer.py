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
    opts = parser.parse_args(args) # comman line arguments
    startTimer(opts.minutes)

def startTimer(minutes):
    message = 'Starting %s minute timer.' % minutes
    os.system('notify-send \'Starting timer\'')
    seconds = minutes * 60
    time.sleep(seconds)
    os.system('notify-send \'Timer is up\'')


if __name__ == '__main__':    
    main(sys.argv[1:])
