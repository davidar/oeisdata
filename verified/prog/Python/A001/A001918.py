from sympy import prime
from sympy.ntheory.residue_ntheory import primitive_root
def A001918(n): return primitive_root(prime(n)) # _Chai Wah Wu_, Sep 13 2022
print([A001918(n) for n in range(1,31)])
