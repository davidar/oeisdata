# faster version for initial segment of sequence
from itertools import count, islice
from sympy import nextprime, perfect_power, primitive_root
def agen(): # generator of terms
    p, adict, n = 2, {None: 0}, 1
    for k in count(1):
        v = primitive_root(p)
        if v not in adict:
            adict[v] = p
        if perfect_power(n): adict[n] = 0
        while n in adict: yield adict[n]; n += 1
        p = nextprime(p)
print(list(islice(agen(), 40))) # _Michael S. Branicky_, Feb 13 2023