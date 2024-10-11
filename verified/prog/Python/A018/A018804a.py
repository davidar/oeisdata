from sympy.ntheory import totient, divisors
print([sum(n*totient(d)//d for d in divisors(n)) for n in range(1, 101)]) # _Indranil Ghosh_, Apr 04 2017