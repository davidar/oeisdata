from math import prod
from itertools import count, accumulate, islice
from sympy import factorint
def A014198_gen(): # generator of terms
    return accumulate(map(lambda n:prod(e+1 if p & 3 == 1 else (e+1) & 1 for p, e in factorint(n).items() if p > 2) << 2, count(1)),initial=0)
A014198_list = list(islice(A014198_gen(),30)) # _Chai Wah Wu_, Jun 28 2022
print(A014198_list)
