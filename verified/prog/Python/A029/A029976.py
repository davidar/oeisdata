from itertools import chain
from sympy import isprime
from gmpy2 import digits
A029976 = sorted((n for n in chain((int(digits(x,8)+digits(x,8)[::-1],8) for x in range(1,8**6)),(int(digits(x,8)+digits(x,8)[-2::-1],8) for x in range(1,8**6))) if isprime(n)))
# _Chai Wah Wu_, Aug 16 2014
print(A029976)
