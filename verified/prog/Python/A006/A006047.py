from sympy.ntheory.factor_ import digits
from sympy import prod
def a(n):
    d=digits(n, 3)
    return n + 1 if n<3 else prod(1 + d[i] for i in range(1, len(d)))
print([a(n) for n in range(51)]) # _Indranil Ghosh_, Jun 06 2017