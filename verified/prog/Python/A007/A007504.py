from itertools import accumulate, count, islice
from sympy import prime
def A007504_gen(): return accumulate(prime(n) if n > 0 else 0 for n in count(0))
A007504_list = list(islice(A007504_gen(),20)) # _Chai Wah Wu_, Feb 23 2022
print(A007504_list)
