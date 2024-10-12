from sympy import isprime
from itertools import count, islice
def agen(): yield from filter(isprime, (int(str(k)+str(k+1)) for k in count(2, 2)))
print(list(islice(agen(), 38))) # _Michael S. Branicky_, Aug 05 2022