from sympy import sqrt, re, I
def a(n): return 2*re(((1 + I*sqrt(7))/2)**n)
print([a(n) for n in range(40)]) # _Indranil Ghosh_, Jun 02 2017