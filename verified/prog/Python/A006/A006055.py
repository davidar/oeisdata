from sympy import isprime
from itertools import count, islice
def bgen(): yield from (int("".join(str((s0+i)%10) for i in range(d))) for d in count(1) for s0 in range(1, 10))
def agen(): yield from filter(isprime, bgen())
print(list(islice(agen(), 18))) # _Michael S. Branicky_, May 26 2022