from sympy import prime
def A027419(n): return len({i*j for i in range(1,prime(n)+1) for j in range(1,i+1)})+1 # _Chai Wah Wu_, Oct 13 2023
print([A027419(n) for n in range(1,31)])
