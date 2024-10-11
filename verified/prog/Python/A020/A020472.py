from sympy import isprime
from itertools import count, islice, product
def agen(): # generator of terms
    for d in count(2):
        for first in product("89", repeat=d-1):
            t = int("".join(first) + "9")
            if isprime(t): yield t
print(list(islice(agen(), 30))) # _Michael S. Branicky_, Nov 15 2022