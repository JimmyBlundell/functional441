import timeit
from multiprocessing import Pool
from get_info import get_char_info
from single_split import get_single_char_info
from double_split import get_double_char_info
from triple_split import get_triple_char_info

start = timeit.default_timer()

""""#Get a list containing total info for single, double, and triple char split
ans = get_char_info()"""# Keep this

text = open("WarAndPeace.txt")
text = list(text)

#TODO: Use original 3 functions. Alter them to stop before they call map() to apply entropy equation.
#TODO: Instead, use the entropy equation as a parameter in the map() function that I parellelize using pool.map. Return list from functions.
#TODO: AKA run the 3 functions before, then create worker pool, then pool.map(list, entropy_equation).

stop = timeit.default_timer()

print('Time: ', stop - start)
