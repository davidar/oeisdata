from math import prod
def a(n): return prod(map(int, str(n)))
print([a(n) for n in range(108)]) # _Michael S. Branicky_, Jan 16 2022