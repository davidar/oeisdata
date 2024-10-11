from sympy import divisor_count
def a(n): return (divisor_count(n**5) + 4)//5
print([a(n) for n in range(1, 101)]) # _Indranil Ghosh_, Apr 14 2017