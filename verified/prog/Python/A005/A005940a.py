from sympy import prime
import math
def A(n): return n - 2**int(math.floor(math.log(n, 2)))
def b(n): return n + 1 if n<2 else prime(1 + (len(bin(n)[2:]) - bin(n)[2:].count("1"))) * b(A(n))
print([b(n - 1) for n in range(1, 101)]) # _Indranil Ghosh_, Apr 10 2017