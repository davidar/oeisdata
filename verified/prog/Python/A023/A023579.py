from sympy import prime
def A023579(n): return (~(m:=prime(n)+3)& m-1).bit_length() # _Chai Wah Wu_, Jul 07 2022
print([A023579(n) for n in range(1,31)])
