from sympy import divisors, totient
def a(n):
    return 1 if n<1 else ((2**(n//2+1) if n%2 else 3*2**(n//2-1)) + sum(totient(n//d)*2**d for d in divisors(n))//n)//2
print([a(n) for n in range(51)]) # _Indranil Ghosh_, Apr 23 2017