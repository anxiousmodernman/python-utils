#!/usr/bin/env python

import time
import os
import cmd


class Timer(cmd.Cmd):

    prompt = '(timer) '

    def do_start(self, line):
        """
        The whole command line is read in as a string. The
        first argument must be an integer representing the number of minutes to sleep,
        and the rest of the line becomes a message to print.
        """
        split_line = line.split()
        minutes = int(split_line[0])
        concatenated_message = ' '.join(split_line[1:])
        os.system('notify-send \' '+ concatenated_message +'\'')
        seconds = minutes * 60
        os.system('notify-send \'Starting ' + str(minutes) + ' minute timer\'')
        time.sleep(seconds)
        os.system('notify-send \'Timer is up\n '+ concatenated_message +'\'')

    def default(self, line):
        self.do_start(line)


if __name__ == '__main__':    
    Timer().cmdloop()
