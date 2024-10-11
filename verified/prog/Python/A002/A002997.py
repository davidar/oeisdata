from itertools import islice
from sympy import nextprime, factorint
def A002997_gen(): # generator of terms
    p, q = 3, 5
    while True:
        for n in range(p+2,q,2):
            f = factorint(n)
            if max(f.values()) == 1 and not any((n-1) % (p-1) for p in f):
                yield n
        p, q = q, nextprime(q)
A002997_list = list(islice(A002997_gen(),20)) # _Chai Wah Wu_, May 11 2022
print(A002997_list)
