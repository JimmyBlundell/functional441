import functools
import math
import logging
import threading
import os
from queue import Queue
from threading import Thread

def get_double_char_info(text):

    num_double_chars = len(text)/2

    # Split up text into groups of doubles
    doubles = list((map(''.join, zip(*[iter(text)] * 2))))

    char_freq = {}

    def getcharfreq(char_freq, ch):
        char_freq[ch] = char_freq.get(ch, 0) + 1
        return char_freq

    # Get the frequencies of each character in the text
    functools.reduce(getcharfreq, doubles, char_freq)

    lst = list(char_freq.values())
    return lst
