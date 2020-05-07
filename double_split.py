import functools
import math

def get_double_char_info(text):

    num_double_chars = len(text)/2

    double_split_equation = lambda x: (x) * (-1) * (x / num_double_chars) * (math.log2(x / num_double_chars))
