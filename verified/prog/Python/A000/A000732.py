from itertools import accumulate, count, islice
from sympy import prime
def A000732_gen(): # generator of terms
    yield 1
    blist = (1,)
    for i in count(1):
        yield (blist := tuple(accumulate(reversed(blist),initial=prime(i))))[-1]
A000732_list = list(islice(A000732_gen(),40)) # _Chai Wah Wu_, Jun 12 2022
print(A000732_list)
