from sympy import primerange
print([n for n in primerange(1, 1001) if bin(n)[2:].count("1")%2]) # _Indranil Ghosh_, May 03 2017