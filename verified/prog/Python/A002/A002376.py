from itertools import count
from sympy.solvers.diophantine.diophantine import power_representation
def A002376(n):
    if n == 1: return 1
    for k in count(1):
        try:
            next(power_representation(n,3,k))
        except:
            continue
        return k # _Chai Wah Wu_, Jun 25 2024
print([A002376(n) for n in range(1,31)])
