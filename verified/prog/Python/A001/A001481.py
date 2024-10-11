from itertools import count, islice
from sympy import factorint
def A001481_gen(): # generator of terms
    return filter(lambda n:(lambda m:all(d & 3 != 3 or m[d] & 1 == 0 for d in m))(factorint(n)),count(0))
A001481_list = list(islice(A001481_gen(),30)) # _Chai Wah Wu_, Jun 27 2022
print(A001481_list)
