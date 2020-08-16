import time
import sys


def animation(process):
    while process.is_alive():
        bar = ["[■□□□□□□□□□]",
               "[■■□□□□□□□□]",
               "[■■■□□□□□□□]",
               "[■■■■□□□□□□]",
               "[■■■■■□□□□□]",
               "[■■■■■■□□□□]",
               "[■■■■■■■□□□]",
               "[■■■■■■■■□□]",
               "[■■■■■■■■■□]",
               "[■■■■■■■■■■]"]

        # chars = "/—\|"
        for e in bar:
            sys.stdout.write('\r' + ' Processing ' + e)
            time.sleep(.2)
            sys.stdout.flush()
