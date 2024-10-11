from sympy.ntheory import divisor_sigma as D
print([i for i in range(1, 10000) if D(D(i, 1), 1)%i==0]) # _Indranil Ghosh_, Mar 17 2017