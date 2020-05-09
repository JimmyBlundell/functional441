import timeit
from get_info import get_char_info

start = timeit.default_timer()

#Get a list containing total info for single, double, and triple char split
ans = get_char_info()

stop = timeit.default_timer()

print('Time: ', stop - start)
