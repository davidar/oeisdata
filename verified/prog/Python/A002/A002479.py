from itertools import count, islice
from sympy import factorint
def A002479_gen(): # generator of terms
    return filter(lambda n:all(p & 7 < 5 or e & 1 == 0 for p, e in factorint(n).items()),count(0))
A002479_list = list(islice(A002479_gen(),30)) # _Chai Wah Wu_, Jun 27 2022
print(A002479_list)
