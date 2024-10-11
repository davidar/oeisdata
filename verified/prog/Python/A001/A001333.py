from functools import cache
@cache
def a(n): return 1 if n < 2 else 2*a(n-1) + a(n-2)
print([a(n) for n in range(32)]) # _Michael S. Branicky_, Nov 13 2022