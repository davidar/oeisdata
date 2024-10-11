from sympy import isprime
from itertools import count, islice, product
def agen(): # generator of terms
    yield 7
    for d in count(2):
        for first in product("67", repeat=d-1):
            t = int("".join(first) + "7")
            if isprime(t): yield t
print(list(islice(agen(), 31))) # _Michael S. Branicky_, Nov 15 2022