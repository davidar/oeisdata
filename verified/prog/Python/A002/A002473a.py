import heapq
from itertools import islice
from sympy import primerange
def A002473gen(p=7): # generate all p-smooth terms
    v, oldv, h, psmooth_primes, = 1, 0, [1], list(primerange(1, p+1))
    while True:
        v = heapq.heappop(h)
        if v != oldv:
            yield v
            oldv = v
            for p in psmooth_primes:
                heapq.heappush(h, v*p)
print(list(islice(A002473gen(), 65))) # _Michael S. Branicky_, Nov 19 2022