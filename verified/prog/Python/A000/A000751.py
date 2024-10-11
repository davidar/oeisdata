from itertools import accumulate, count, islice
from sympy import npartitions
def A000751_gen(): # generator of terms
    blist = tuple()
    for i in count(0):
        yield (blist := tuple(accumulate(reversed(blist),initial=npartitions(i))))[-1]
A000751_list = list(islice(A000751_gen(),40)) # _Chai Wah Wu_, Jun 12 2022
print(A000751_list)
