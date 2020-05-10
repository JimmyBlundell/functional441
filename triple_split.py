import functools
import math
import logging
import threading
import os
from queue import Queue
from threading import Thread

def get_triple_char_info(text):

    num_triple_chars = len(text)/3

    # Split up text into groups of triples
    triples = list((map(''.join, zip(*[iter(text)] * 3))))

    char_freq = {}

    def getcharfreq(char_freq, ch):
        char_freq[ch] = char_freq.get(ch, 0) + 1
        return char_freq

    # Get the frequencies of each character in the text
    functools.reduce(getcharfreq, triples, char_freq)

    lst = list(char_freq.values())
    return lst