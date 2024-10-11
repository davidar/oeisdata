from itertools import count, islice
from sympy import nextprime, is_nthpow_residue
def A014755_gen(startvalue=2): # generator of terms >= startvalue
    p = max(nextprime(startvalue-1),2)
    while True:
        if p&7==1 and is_nthpow_residue(3,4,p) and is_nthpow_residue(-3,4,p):
            yield p
        p = nextprime(p)
A014755_list = list(islice(A014755_gen(),20)) # _Chai Wah Wu_, May 02 2024
print(A014755_list)
