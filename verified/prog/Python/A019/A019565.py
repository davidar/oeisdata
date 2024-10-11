from operator import mul
from functools import reduce
from sympy import prime
def A019565(n):
    return reduce(mul,(prime(i+1) for i,v in enumerate(bin(n)[:1:-1]) if v == '1')) if n > 0 else 1
# _Chai Wah Wu_, Dec 25 2014
print([A019565(n) for n in range(30)])
