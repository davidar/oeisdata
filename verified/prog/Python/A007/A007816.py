from math import factorial
def A007816(n): return ((n*(n + 5) + 6)*factorial((n<<2)+1)>>1)//factorial(3*(n+1)) # _Chai Wah Wu_, Nov 17 2022
print([A007816(n) for n in range(1,31)])
