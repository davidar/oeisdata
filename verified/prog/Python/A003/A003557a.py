from sympy.ntheory.factor_ import core
from sympy import divisors
def a(n): return n / max(i for i in divisors(n) if core(i) == i)
print([a(n) for n in range(1, 101)]) # _Indranil Ghosh_, Apr 16 2017