from sympy.ntheory.primetest import is_square
def A000122(n): return is_square(n)<<1 if n else 1 # _Chai Wah Wu_, May 17 2023
print([A000122(n) for n in range(30)])
