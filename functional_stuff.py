import functools
from collections import Counter

text = open("WarAndPeace.txt")

text = str(list(text))

charfreq = {}

def getcharfreq(charfreq, ch):
    charfreq[ch] = charfreq.get(ch, 0) + 1
    return charfreq

functools.reduce(getcharfreq, text, charfreq)

print(charfreq)