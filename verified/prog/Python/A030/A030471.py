from sympy import isprime
from itertools import count, islice
def agen(): # generator of terms
    strs = ["1", "2", "3", "4"]
    for k in count(1):
        if isprime(t:=int("".join(strs))): yield t
        strs = strs[1:] + [str(k+4)]
print(list(islice(agen(), 20))) # _Michael S. Branicky_, Aug 26 2024