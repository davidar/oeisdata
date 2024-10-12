from itertools import combinations_with_replacement
from gmpy2 import is_square
A028820_list = [0] + [n for n in (int(''.join(i)) for l in range(1,11) for i in combinations_with_replacement('123456789',l)) if is_square(n)] # _Chai Wah Wu_, Dec 07 2015
print(A028820_list)
