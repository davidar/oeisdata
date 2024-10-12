from sympy import totient, divisors
def A026119(n):
    m = (n<<1)+1
    return sum(totient(d)<<m//d-1 for d in divisors(m,generator=True))//m # _Chai Wah Wu_, Feb 21 2023
print([A026119(n) for n in range(30)])
