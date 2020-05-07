import functools
import math
from collections import Counter

equation = lambda nc, pc : (nc)*(-1)*(pc)*(math.log2(pc))

text = open("WarAndPeace.txt")

text = str(list(text))

char_freq = {}

def getcharfreq(charfreq, ch):
    charfreq[ch] = charfreq.get(ch, 0) + 1
    return charfreq

# Get the frequencies of each character in the text
functools.reduce(getcharfreq, text, char_freq)

print(char_freq)

total_chars = len(char_freq) # Use this in lambda equation to get probability of characters: #occurences/#characters

#TODO: Find a way to use the equation to do a summation over all the char frequencies in char_freq to get total information
#TODO: Repeat for pairs and triples, then figure out concurrency.