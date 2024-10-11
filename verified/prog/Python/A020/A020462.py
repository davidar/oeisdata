from gmpy2 import is_prime, mpz
from itertools import product
A020462_list = [int(''.join(x)) for n in range(1,10) for x in product('35',repeat=n) if is_prime(mpz(''.join(x)))] # _Chai Wah Wu_, Jul 21 2015
print(A020462_list)
