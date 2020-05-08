from multiprocessing import Pool
import functools
import math
import timeit
#from single_split import get_single_char_info
#from double_split import get_double_char_info
#from triple_split import get_triple_char_info

def get_single_char_info(text):

    num_single_chars = len(text)

    single_split_equation = lambda x: (x) * (-1) * (x / num_single_chars) * (math.log2(x / num_single_chars))

    char_freq = {}

    def getcharfreq(char_freq, ch):
        char_freq[ch] = char_freq.get(ch, 0) + 1
        return char_freq

    # Get the frequencies of each character in the text
    functools.reduce(getcharfreq, text, char_freq)

    # Using map() to apply entropy equation on each frequency in char_freq, outputting list
    lst = list(map(single_split_equation, char_freq.values()))

    # Sum together values in list for total info
    single_char_info = sum(lst)

    ans = str("Single character split: " + str(single_char_info))
    return ans

def get_double_char_info(text):

    num_double_chars = len(text)/2

    double_split_equation = lambda x: (x) * (-1) * (x / num_double_chars) * (math.log2(x / num_double_chars))

    # Split up text into groups of doubles
    doubles = list((map(''.join, zip(*[iter(text)] * 2))))

    char_freq = {}

    def getcharfreq(char_freq, ch):
        char_freq[ch] = char_freq.get(ch, 0) + 1
        return char_freq

    # Get the frequencies of each character in the text
    functools.reduce(getcharfreq, doubles, char_freq)

    # Using map() to apply entropy equation on each frequency in char_freq, outputting list
    lst = list(map(double_split_equation, char_freq.values()))

    # Sum together values in list for total info
    double_char_info = sum(lst)

    ans = str("Double character split: " + str(double_char_info))
    return ans

def get_triple_char_info(text):

    num_triple_chars = len(text)/3

    triple_split_equation = lambda x: (x) * (-1) * (x / num_triple_chars) * (math.log2(x / num_triple_chars))

    # Split up text into groups of triples
    triples = list((map(''.join, zip(*[iter(text)] * 3))))

    char_freq = {}

    def getcharfreq(char_freq, ch):
        char_freq[ch] = char_freq.get(ch, 0) + 1
        return char_freq

    # Get the frequencies of each character in the text
    functools.reduce(getcharfreq, triples, char_freq)

    # Using map() to apply entropy equation on each frequency in char_freq, outputting list
    lst = list(map(triple_split_equation, char_freq.values()))

    # Sum together values in list for total info
    triple_char_info = sum(lst)

    ans = str("Triple character split: " + str(triple_char_info))
    return ans



def parellelize_me():
    start = timeit.default_timer()

    text = open("WarAndPeace.txt")

    text_single = str(list(text))
    text_double = str(list(text))
    text_triple = str(list(text))

    p = Pool(16)
    ans = p.map(get_single_char_info, text)


    # TODO: Concurrency

    stop = timeit.default_timer()

    print('Time: ', stop - start)




if __name__ == '__main__':
    parellelize_me()








#t1 = threading.Thread(target=get_single_char_info, args=(text,))
#t2 = threading.Thread(target=get_double_char_info, args=(text,))
#t3 = threading.Thread(target=get_triple_char_info, args=(text,))

#t1.start()
#t2.start()
#t3.start()

#t1.join()
#t2.join()
#t3.join()

#get_single_char_info(text)

#get_double_char_info(text)

#get_triple_char_info(text)