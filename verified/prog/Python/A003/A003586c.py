# faster for initial segment of sequence
import heapq
from itertools import islice
def A003586gen(): # generator of terms
    v, oldv, h, psmooth_primes, = 1, 0, [1], [2, 3]
    while True:
        v = heapq.heappop(h)
        if v != oldv:
            yield v
            oldv = v
            for p in psmooth_primes:
                    heapq.heappush(h, v*p)
print(list(islice(A003586gen(), 65))) # _Michael S. Branicky_, Sep 17 2024