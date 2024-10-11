from itertools import combinations_with_replacement
from math import prod
from collections import Counter
def A016728(n):
    if n == 0: return 1
    x, y = (2*n-1)**2, (2*n+1)**2
    return sum(6//prod((1,1,2,6)[d] for d in q.values())<<3-q[0] for q in map(Counter,combinations_with_replacement(range(n+1),3)) if x <= sum(b*a**2 for a, b in q.items())<<2 <= y) # _Chai Wah Wu_, Jun 20 2024
print([A016728(n) for n in range(30)])
