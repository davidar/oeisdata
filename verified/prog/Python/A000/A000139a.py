from sympy import binomial
def A000139(n): return (binomial(3*n, n)*2)//((n+1)*(2*n+1))
print([A000139(n) for n in range(30)])
