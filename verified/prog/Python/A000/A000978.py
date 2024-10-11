from gmpy2 import divexact
from sympy import prime, isprime
A000978 = [p for p in (prime(n) for n in range(2,10**2)) if isprime(divexact(2**p+1,3))] # _Chai Wah Wu_, Sep 04 2014
print(A000978)
