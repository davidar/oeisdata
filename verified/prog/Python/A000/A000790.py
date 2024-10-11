from sympy import isprime
def A000790(n):
    c = 4
    while pow(n,c,c) != (n % c) or isprime(c):
        c += 1
    return c # _Chai Wah Wu_, Apr 02 2021
print([A000790(n) for n in range(30)])
