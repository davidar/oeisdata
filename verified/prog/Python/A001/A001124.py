from itertools import islice
from sympy import nextprime, primitive_root
def A001124_gen(): # generator of terms
    p = 5
    while (p:=nextprime(p)):
        if primitive_root(p)==5:
            yield p
A001124_list = list(islice(A001124_gen(),30)) # _Chai Wah Wu_, Feb 13 2023
print(A001124_list)
