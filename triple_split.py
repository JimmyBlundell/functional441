import functools
import math
import logging
import threading
import os
from queue import Queue
from threading import Thread

def get_triple_char_info(text):

    num_triple_chars = len(text)/3

    #triple_split_equation = lambda x: (x) * (-1) * (x / num_triple_chars) * (math.log2(x / num_triple_chars))

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

    # Using map() to apply entropy equation on each frequency in char_freq, outputting list
    #lst = list(map(triple_split_equation, char_freq.values()))

    # Sum together values in list for total info
    #triple_char_info = sum(lst)

    #ans = str("Triple character split: " + str(triple_char_info))
    #return ans

