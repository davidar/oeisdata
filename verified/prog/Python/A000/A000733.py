from itertools import count, accumulate, islice
from sympy import npartitions
def A000733_gen(): # generator of terms
    yield 1
    blist = (1,)
    for i in count(0):
        yield (blist := tuple(accumulate(reversed(blist),initial=npartitions(i))))[-1]
A000733_list = list(islice(A000733_gen(),40)) # _Chai Wah Wu_, Jun 12 2022
print(A000733_list)
