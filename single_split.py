import functools
import math
import logging
import threading
import os
from queue import Queue
from threading import Thread

def get_single_char_info(text):

    num_single_chars = len(text)

    single_split_equation = lambda x: (x) * (-1) * (x / num_single_chars) * (math.log2(x / num_single_chars))

    char_freq = {}

    def getcharfreq(char_freq, ch):
        char_freq[ch] = char_freq.get(ch, 0) + 1
        return char_freq

    # Get the frequencies of each character in the text
    functools.reduce(getcharfreq, text, char_freq)

    # Using map() to apply entropy equation on each frequency in char_freq, outputting list
    lst = list(map(single_split_equation, char_freq.values()))

    # Sum together values in list for total info
    single_char_info = sum(lst)

    ans = str("Single character split: " + str(single_char_info))
    return ans
