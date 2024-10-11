from sympy import nextprime
from itertools import islice
def agen(): # generator of terms
    yield 3
    p, q = 5, 7
    while True:
        if q - p == 2: yield from [p, q]
        p, q = q, nextprime(q)
print(list(islice(agen(), 58))) # _Michael S. Branicky_, Apr 30 2022