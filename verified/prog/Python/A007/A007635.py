from sympy import isprime
it = (n**2 + n + 17 for n in range(250))
print([p for p in it if isprime(p)]) # _Indranil Ghosh_, Mar 18 2017