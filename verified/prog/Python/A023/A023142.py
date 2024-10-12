from sympy import totient, n_order, divisors
def A023142(n):
    m = n>>(~n & n-1).bit_length()
    a, b = divmod(m,5)
    while not b:
        m = a
        a, b = divmod(m,5)
    return sum(totient(d)//n_order(10,d) for d in divisors(m,generator=True) if d>1)+1 # _Chai Wah Wu_, Apr 09 2024
print([A023142(n) for n in range(1,31)])
