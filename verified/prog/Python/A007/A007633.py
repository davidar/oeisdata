from itertools import chain
from gmpy2 import digits
A007633_list = sorted([n for n in chain((int(str(x)+str(x)[::-1]) for x in range(1,10**6)),(int(str(x)+str(x)[-2::-1]) for x in range(10**6))) if digits(n,3) == digits(n,3)[::-1]]) # _Chai Wah Wu_, Nov 23 2014
print(A007633_list)
