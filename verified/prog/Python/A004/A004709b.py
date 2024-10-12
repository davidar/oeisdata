from sympy import mobius, integer_nthroot
def A004709(n):
    def f(x): return n+x-sum(mobius(k)*(x//k**3) for k in range(1, integer_nthroot(x,3)[0]+1))
    m, k = n, f(n)
    while m != k:
        m, k = k, f(k)
    return m # _Chai Wah Wu_, Aug 05 2024
print([A004709(n) for n in range(1,31)])
