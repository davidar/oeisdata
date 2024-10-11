from sympy import isprime
from itertools import count, islice, product
def agen(): # generator of terms
    yield from [2, 3]
    for d in count(2):
        for first in product("23", repeat=d-1):
            t = int("".join(first) + "3")
            if isprime(t): yield t
print(list(islice(agen(), 34))) # _Michael S. Branicky_, Jun 08 2022