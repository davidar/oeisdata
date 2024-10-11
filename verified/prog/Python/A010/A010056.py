from sympy.ntheory.primetest import is_square
def A010056(n): return int(is_square(m:=5*n**2-4) or is_square(m+8)) # _Chai Wah Wu_, Mar 30 2023
print([A010056(n) for n in range(30)])
