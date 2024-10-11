from itertools import count, islice
from functools import reduce
from math import prod
from sympy import factorint
def A001599_gen(startvalue=1): # generator of terms >= startvalue
    for n in count(max(startvalue,1)):
        f = factorint(n)
        s = prod((p**(e+1)-1)//(p-1) for p, e in f.items())
        if not reduce(lambda x,y:x*y%s,(e+1 for e in f.values()),1)*n%s:
            yield n
A001599_list = list(islice(A001599_gen(),20)) # _Chai Wah Wu_, Feb 14 2023
print(A001599_list)
