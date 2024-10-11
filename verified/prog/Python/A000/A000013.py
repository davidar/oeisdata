from sympy import divisors, totient
def a(n): return 1 if n<1 else sum([totient(2*d)*2**(n/d) for d in divisors(n)])/(2*n) # _Indranil Ghosh_, Apr 28 2017
print([a(n) for n in range(30)])
