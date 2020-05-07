import functools
import math

def get_triple_char_info(text):

    num_triple_chars = len(text)/3

    triple_split_equation = lambda x: (x) * (-1) * (x / num_triple_chars) * (math.log2(x / num_triple_chars))

    # Split up text into groups of triples
    test = list((map(''.join, zip(*[iter(text)] * 3))))