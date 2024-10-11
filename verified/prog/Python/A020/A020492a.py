from sympy import totient, divisor_sigma
print([n for n in range(1, 4001) if divisor_sigma(n)%totient(n)==0]) # _Indranil Ghosh_, Jul 06 2017