from sympy import totient, n_order, divisors
def A023137(n):
    a, b = divmod(n,5)
    while not b:
        n = a
        a, b = divmod(n,5)
    return sum(totient(d)//n_order(5,d) for d in divisors(n,generator=True) if d>1)+1 # _Chai Wah Wu_, Apr 09 2024
print([A023137(n) for n in range(1,31)])
