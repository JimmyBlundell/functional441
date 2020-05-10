import functools
import math


def get_single_char_info(text):

    text = str(text)

    num_single_chars = len(text)

    char_freq = {}

    def getcharfreq(char_freq, ch):
        char_freq[ch] = char_freq.get(ch, 0) + 1
        return char_freq

    # Get the frequencies of each character in the text
    functools.reduce(getcharfreq, text, char_freq)

    lst = list(char_freq.values())
    return lst

