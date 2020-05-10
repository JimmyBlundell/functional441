import math
import timeit
from multiprocessing import Pool
from single_split import get_single_char_info
from double_split import get_double_char_info
from triple_split import get_triple_char_info

text = open("WarAndPeace.txt")
text = list(text)
text = str(text)

num_single_chars = len(text)
num_double_chars = len(text) / 2
num_triple_chars = len(text) / 3

def single_entropy(x):
    return ((x) * (-1) * (x / num_single_chars) * (math.log2(x / num_single_chars)))

def double_entropy(x):
    return ((x) * (-1) * (x / num_double_chars) * (math.log2(x / num_double_chars)))

def triple_entropy(x):
    return ((x) * (-1) * (x / num_triple_chars) * (math.log2(x / num_triple_chars)))


if __name__ == '__main__':
    start = timeit.default_timer()

    lst1 = get_single_char_info(text)
    lst2 = get_double_char_info(text)
    lst3 = get_triple_char_info(text)

    stop = timeit.default_timer()

    t1 = (stop - start)

    with Pool(processes=64) as pool:
        start = timeit.default_timer()
        ans1 = ((pool.map(single_entropy, lst1)))
        ans2 = ((pool.map(double_entropy, lst2)))
        ans3 = ((pool.map(triple_entropy, lst3)))
        stop = timeit.default_timer()

    print('Time: ', (stop - start) + t1)

    print(sum(ans1))
    print(sum(ans2))
    print(sum(ans3))
