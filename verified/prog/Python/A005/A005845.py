from sympy import isprime
from itertools import count, islice
def agen(): # generator of terms
    L0, L1 = 2, 1
    for k in count(1):
        L0, L1 = L1, L0+L1
        if k > 1 and not isprime(k) and (L0-1)%k == 0:
            yield k
print(list(islice(agen(), 32))) # _Michael S. Branicky_, Apr 07 2024