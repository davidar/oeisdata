from itertools import islice
from sympy import nextprime, is_primitive_root
def A001123_gen(): # generator of terms
    p = 3
    while (p:=nextprime(p)):
        if not is_primitive_root(2,p) and is_primitive_root(3,p):
            yield p
A001123_list = list(islice(A001123_gen(),30)) # _Chai Wah Wu_, Feb 13 2023
print(A001123_list)
