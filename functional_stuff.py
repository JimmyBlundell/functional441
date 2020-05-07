import functools
import math
from collections import Counter

# Lambda expression for finding total info
equation = lambda x: (x)*(-1)*(x/num_chars)*(math.log2(x/num_chars))

text = open("WarAndPeace.txt")

text = str(list(text))

num_chars = len(text)

char_freq = {}

def getcharfreq(char_freq, ch):
    char_freq[ch] = char_freq.get(ch, 0) + 1
    return char_freq

# Get the frequencies of each character in the text
functools.reduce(getcharfreq, text, char_freq)

#total_chars = len(char_freq) # Use this in lambda equation to get probability of characters: #occurences/#characters

items = list(char_freq.items()) # Turn into list to iterate through in map() function - Don't know if I need?

test = list(map(equation, char_freq.values()))

single_char_info = sum(test)

print(single_char_info
      )
# TODO: Repeat for pairs and triples, then figure out concurrency.