from sympy import lucas
def A022801(n):
    def f(x):
        if x<=2: return n+1
        a, b, c = 1, 3, 0
        while b<=x:
            a, b = b, a+b
            c += 1
        return n+1+c
    m, k = n+1, f(n+1)
    while m != k: m, k = k, f(k)
    return m+lucas(n) # _Chai Wah Wu_, Sep 10 2024
print([A022801(n) for n in range(1,31)])
