from sympy import isprime
print([n for n in range(1, 200) if n%2 and not isprime(n + 2)]) # _Indranil Ghosh_, Jun 15 2017, after _Charles R Greathouse IV_