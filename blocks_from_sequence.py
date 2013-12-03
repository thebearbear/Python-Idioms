def chunker(seq, size):
    for i in range(0, len(seq), size):
      yield s[i:i+size] 


# taken from http://docs.python.org/2.7/library/itertools.html#recipes
from itertools import izip_longest
def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)
