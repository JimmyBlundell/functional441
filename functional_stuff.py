import math
from single_split import get_single_char_info

text = open("WarAndPeace.txt")

text = str(list(text))

get_single_char_info(text)

# TODO: Repeat for pairs and triples, then figure out concurrency.