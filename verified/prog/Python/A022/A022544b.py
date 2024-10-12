from itertools import count, islice
from sympy import factorint
def A022544_gen(): # generator of terms
    return filter(lambda n:any(p & 3 == 3 and e & 1 for p, e in factorint(n).items()),count(0))
A022544_list = list(islice(A022544_gen(),30)) # _Chai Wah Wu_, Jun 28 2022
print(A022544_list)
