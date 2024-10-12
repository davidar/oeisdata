from math import prod
def A028362(n): return prod((1<<i)+1 for i in range(1,n)) # _Chai Wah Wu_, Jun 20 2022
print([A028362(n) for n in range(1,31)])
