from sympy import totient, divisors, isprime, prod
def a(m):
    if m == 1: return 2
    if m % 2: return 0
    X = (x + 1 for x in divisors(m))
    nmax=m*prod(i/(i - 1) for i in X if isprime(i))
    n=m
    k=0
    while n<=nmax:
        if totient(n)==m:k+=1
        n+=1
    return k
print([a(n) for n in range(1, 51)]) # _Indranil Ghosh_, Jul 18 2017, after Mathematica code