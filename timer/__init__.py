__author__ = 'coleman'

import time
import os


start_time = time.time()

def startTimer():
    message = 'Starting 10 minute timer.'
    os.system('notify-send \'Starting 10 minute timer\'')
    time.sleep(600)
    os.system('notify-send \'10 minutes are up\'')

