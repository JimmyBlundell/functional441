import functools
import math

def get_triple_char_info(text):

    num_triple_chars = len(text)/3

    triple_split_equation = lambda x: (x) * (-1) * (x / num_triple_chars) * (math.log2(x / num_triple_chars))
