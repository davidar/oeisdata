from math import prod
from itertools import count, islice
from sympy import factorint
def A023897_gen(startvalue=1): # generator of terms >= startvalue
    for m in count(max(startvalue,1)):
        f = factorint(m)
        q, r = divmod(prod(p**(e+2)-p for p,e in f.items()),m*prod((p-1)**2 for p in f))
        if not r:
            yield q
A023897_list = list(islice(A023897_gen(),20)) # _Chai Wah Wu_, Aug 12 2024
print(A023897_list)
