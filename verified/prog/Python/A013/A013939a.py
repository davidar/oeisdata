from sympy.ntheory import primefactors
print([sum(len(primefactors(k)) for k in range(1,n+1)) for n in range(1, 121)]) # _Indranil Ghosh_, Mar 19 2017