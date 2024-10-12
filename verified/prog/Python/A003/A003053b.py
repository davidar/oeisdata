from math import prod
def A003053(n): return (1 << (n//2)**2)*prod((1 << i)-1 for i in range(2,2*((n-1)//2)+1,2)) # _Chai Wah Wu_, Jun 20 2022
print([A003053(n) for n in range(1,31)])
