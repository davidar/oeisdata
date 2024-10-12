from sympy import totient, n_order, divisors
def A023141(n):
    a, b = divmod(n,3)
    while not b:
        n = a
        a, b = divmod(n,3)
    return sum(totient(d)//n_order(9,d) for d in divisors(n,generator=True) if d>1)+1 # _Chai Wah Wu_, Apr 09 2024
print([A023141(n) for n in range(1,31)])
