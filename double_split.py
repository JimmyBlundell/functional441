import functools
import math
import logging
import threading
import os
from queue import Queue
from threading import Thread

def get_double_char_info(text):

    num_double_chars = len(text)/2

    #double_split_equation = lambda x: (x) * (-1) * (x / num_double_chars) * (math.log2(x / num_double_chars))

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

    # Using map() to apply entropy equation on each frequency in char_freq, outputting list
    #lst = list(map(double_split_equation, char_freq.values()))

    # Sum together values in list for total info
    #double_char_info = sum(lst)

    #ans = str("Double character split: " + str(double_char_info))
    #return ans

