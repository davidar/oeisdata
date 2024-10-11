from sympy import divisor_count, npartitions
def a(n): return sum([divisor_count(m)*npartitions(n - m) for m in range(1, n + 1)]) # _Indranil Ghosh_, Apr 25 2017
print([a(n) for n in range(30)])
