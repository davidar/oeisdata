from math import gcd
from itertools import count, islice
from sympy import isprime, divisor_sigma
def A003624_gen(startvalue=2): # generator of terms
    return filter(lambda k:not isprime(k) and gcd(k,divisor_sigma(k))==1,count(max(startvalue,2)))
A003624_list = list(islice(A003624_gen(),30)) # _Chai Wah Wu_, Jul 06 2023
print(A003624_list)
