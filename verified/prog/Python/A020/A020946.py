from itertools import count
from functools import reduce
def A020946(n): return next(filter(lambda k:sum(reduce(lambda x,y:(x[0],x[0]+x[1]) if int(y) else (x[0]+x[1],x[1]),bin(k)[-1:2:-1],(1,0)))==n,count(1))) if n else 0 # _Chai Wah Wu_, May 05 2023
print([A020946(n) for n in range(30)])
