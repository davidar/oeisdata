from sympy import nextprime
from itertools import islice
def agen(): # generator of terms
    p, q, r, s = [2, 3, 5, 7]
    while True:
        if p + s == q + r: yield p
        p, q, r, s = q, r, s, nextprime(s)
print(list(islice(agen(), 50))) # _Michael S. Branicky_, May 31 2024