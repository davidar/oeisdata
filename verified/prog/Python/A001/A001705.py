from math import factorial
def A001705(n):
    f = factorial(n)
    return sum(f*(k+1)//(n-k) for k in range(n)) # _Chai Wah Wu_, Jun 23 2022
print([A001705(n) for n in range(30)])
