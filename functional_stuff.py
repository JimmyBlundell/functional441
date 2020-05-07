from single_split import get_single_char_info
from double_split import get_double_char_info
from triple_split import get_triple_char_info

text = open("WarAndPeace.txt")

text = str(list(text))

get_single_char_info(text)

get_double_char_info(text)

get_triple_char_info(text)

# TODO: Concurrency