from functools import cache
@cache
def a(n): return [1, 3][n-1] if n < 3 else a(n-1) + a(n-2)
print([a(n) for n in range(1, 41)]) # _Michael S. Branicky_, Nov 13 2022