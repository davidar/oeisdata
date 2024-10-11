from itertools import islice
from sympy import nextprime, is_primitive_root
def A001122_gen(): # generator of terms
    p = 2
    while (p:=nextprime(p)):
        if is_primitive_root(2,p):
            yield p
A001122_list = list(islice(A001122_gen(),30)) # _Chai Wah Wu_, Feb 13 2023
print(A001122_list)
