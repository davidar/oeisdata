from sympy import factorint
from itertools import count, islice
def sopf(n): return sum(p*e for p, e in factorint(n).items())
def agen(): # generator of terms
    sopfkplus1 = 2
    for k in count(2):
        sopfk, sopfkplus1 = sopfkplus1, sopf(k+1)
        if k + sopfk == k + 1 + sopfkplus1: yield k
print(list(islice(agen(), 42))) # _Michael S. Branicky_, Apr 15 2022