from sympy.ntheory.primetest import is_square
def A023532(n): return bool(is_square((n<<3)+9))^1 # _Chai Wah Wu_, Feb 10 2023
print([A023532(n) for n in range(30)])
