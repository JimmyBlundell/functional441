import functools
import math
from collections import Counter

# Lambda expression for finding total info
equation = lambda x: (x)*(-1)*(x/num_chars)*(math.log2(x/num_chars))

text = open("WarAndPeace.txt")

text = str(list(text))

num_chars = len(text) # Used for calculating probability

char_freq = {}

def getcharfreq(char_freq, ch):
    char_freq[ch] = char_freq.get(ch, 0) + 1
    return char_freq

# Get the frequencies of each character in the text
functools.reduce(getcharfreq, text, char_freq)

# Using map() to apply entropy equation on each frequency in char_freq, outputting list
test = list(map(equation, char_freq.values()))

# Sum together values in list for total info
single_char_info = sum(test)

print(single_char_info)


# TODO: Repeat for pairs and triples, then figure out concurrency.