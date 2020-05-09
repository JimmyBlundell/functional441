import functools
import math

def get_char_info():

    ans = []

    text = open("WarAndPeace.txt")

    # Convert to string - not sure if necessary
    text = str(list(text))

    num_single_chars = len(text)
    num_double_chars = num_single_chars/2
    num_triple_chars = num_single_chars/3


    # Lambda equations for calculating entropy for each split
    single_split_equation = lambda x: (x) * (-1) * (x / num_single_chars) * (math.log2(x / num_single_chars))
    double_split_equation = lambda x: (x) * (-1) * (x / num_double_chars) * (math.log2(x / num_double_chars))
    triple_split_equation = lambda x: (x) * (-1) * (x / num_triple_chars) * (math.log2(x / num_triple_chars))

    # Split up text into groups of doubles and triples
    doubles = list((map(''.join, zip(*[iter(text)] * 2))))
    triples = list((map(''.join, zip(*[iter(text)] * 3))))


    # Dictionaries to hold the frequencies of chars depending on split
    single_char_freq = {}
    double_char_freq = {}
    triple_char_freq = {}

    def getcharfreq(char_freq, ch):
        char_freq[ch] = char_freq.get(ch, 0) + 1
        return char_freq

    # Get the character frequencies, finally
    functools.reduce(getcharfreq, text, single_char_freq)
    functools.reduce(getcharfreq, doubles, double_char_freq)
    functools.reduce(getcharfreq, triples, triple_char_freq)

    #TODO: map() function is not working right now - need to find out why
    # Using map() to apply entropy equation on each frequency in char_freq, outputting list
    lst_single = list(map(single_split_equation, single_char_freq.values()))
    lst_double = list(map(double_split_equation, double_char_freq.values()))
    lst_triple = list(map(triple_split_equation, triple_char_freq.values()))

    # Sum together values in list for total info
    single_char_info = sum(lst_single)
    double_char_info = sum(lst_double)
    triple_char_info = sum(lst_triple)

    # Return a list of final values
    ans.append(str(("Single character split: " + str(single_char_info))))
    ans.append(str(("Double character split: " + str(double_char_info))))
    ans.append(str(("Triple character split: " + str(triple_char_info))))

    return ans