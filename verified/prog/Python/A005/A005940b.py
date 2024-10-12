from math import prod
from itertools import accumulate
from collections import Counter
from sympy import prime
def A005940(n): return prod(prime(len(a)+1)**b for a, b in Counter(accumulate(bin(n-1)[2:].split('1')[:0:-1])).items()) # _Chai Wah Wu_, Mar 10 2023
print([A005940(n) for n in range(1,31)])
