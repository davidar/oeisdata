from operator import mul
from functools import reduce
A007602 = [n for n in range(1,10**5) if not (str(n).count('0') or n % reduce(mul, (int(d) for d in str(n))))] # _Chai Wah Wu_, Aug 25 2014
print(A007602)
