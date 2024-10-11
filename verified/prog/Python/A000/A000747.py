from itertools import islice, count, accumulate
from sympy import prime
def A000747_gen(): # generator of terms
    blist = tuple()
    for i in count(1):
        yield (blist := tuple(accumulate(reversed(blist),initial=prime(i))))[-1]
A000747_list = list(islice(A000747_gen(),30)) # _Chai Wah Wu_, Jun 11 2022
print(A000747_list)
