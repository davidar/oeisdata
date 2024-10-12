from sympy import sqrt
import math
r=(1 + sqrt(5))/2
def a(n): return 1 if n<1 else int(math.floor((n - 1)*r)) + n + 1
print([a(n) for n in range(1, 101)]) # _Indranil Ghosh_, Mar 25 2017