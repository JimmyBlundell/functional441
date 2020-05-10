import math
import timeit
from multiprocessing import Pool
from get_info import get_char_info
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

#single_split_equation = lambda x: (x) * (-1) * (x / num_single_chars) * (math.log2(x / num_single_chars))
#double_split_equation = lambda x: (x) * (-1) * (x / num_double_chars) * (math.log2(x / num_double_chars))
#triple_split_equation = lambda x: (x) * (-1) * (x / num_triple_chars) * (math.log2(x / num_triple_chars))


if __name__ == '__main__':
    start = timeit.default_timer()


    lst1 = get_single_char_info(text)
    lst2 = get_double_char_info(text)
    lst3 = get_triple_char_info(text)

    stop = timeit.default_timer()
    print('Time: ', stop - start)

    with Pool(processes=64) as pool:
        start = timeit.default_timer()
        ans1 = list((pool.map(single_entropy, lst1)))
        ans2 = list((pool.map(double_entropy, lst2)))
        ans3 = list((pool.map(triple_entropy, lst3)))

    stop = timeit.default_timer()

    print('Time: ', stop - start)

    print(sum(ans1))
    print(sum(ans2))
    print(sum(ans3))

    #TODO: Use original 3 functions. Alter them to stop before they call map() to apply entropy equation.
    #TODO: Instead, use the entropy equation as a parameter in the map() function that I parellelize using pool.map. Return list from functions.
    #TODO: AKA run the 3 functions before, then create worker pool, then pool.map(list, entropy_equation).

    #stop = timeit.default_timer()

    #print('Time: ', stop - start)
