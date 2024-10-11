# Python 3.2 or higher required
from itertools import accumulate
from sympy import isprime
A002496_list = [n+1 for n in accumulate(range(10**5),lambda x,y:x+2*y-1) if isprime(n+1)] # _Chai Wah Wu_, Sep 23 2014
print(A002496_list)
