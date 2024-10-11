from itertools import product
from sympy import isprime
A019546_list = [2,3,5,7]+[p for p in (int(''.join(d)+e) for l in range(1,5) for d in product('2357',repeat=l) for e in '37') if isprime(p)] # _Chai Wah Wu_, Jun 04 2021
print(A019546_list)
