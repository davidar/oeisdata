from sympy import divisor_sigma
from itertools import count, islice
def A005100_gen(startvalue=1): return filter(lambda n:divisor_sigma(n) < 2*n,count(max(startvalue,1))) # generator of terms >= startvalue
A005100_list = list(islice(A005100_gen(),20)) # _Chai Wah Wu_, Jan 14 2022
print(A005100_list)
