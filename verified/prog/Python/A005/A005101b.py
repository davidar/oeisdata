from sympy import divisor_sigma
from itertools import count, islice
def A005101_gen(startvalue=1): return filter(lambda n:divisor_sigma(n) > 2*n, count(max(startvalue, 1))) # generator of terms >= startvalue
A005101_list = list(islice(A005101_gen(), 20)) # _Chai Wah Wu_, Jan 14 2022
print(A005101_list)
