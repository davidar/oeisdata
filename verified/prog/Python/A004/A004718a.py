# from first formula
from functools import reduce
def f(s, b): return s + 1 if b == '1' else -s
def a(n): return reduce(f, [0] + list(bin(n)[2:]))
print([a(n) for n in range(86)]) # _Michael S. Branicky_, Apr 03 2021