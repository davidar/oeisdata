from itertools import count, islice
from sympy import factorint
def A020893_gen(): # generator of terms
    return filter(lambda n:all(p & 3 != 3 and e == 1 for p, e in factorint(n).items()),count(1))
A020893_list = list(islice(A020893_gen(),30)) # _Chai Wah Wu_, Jun 28 2022
print(A020893_list)
