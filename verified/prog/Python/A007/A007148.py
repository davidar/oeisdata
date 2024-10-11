from sympy import divisors, totient
def a(n):
    if n==1: return 1
    return 2**(n - 2) + sum(totient(2*d)*2**(n//d) for d in divisors(n))//(4*n)
print([a(n) for n in range(1, 31)]) # _Indranil Ghosh_, Jul 24 2017