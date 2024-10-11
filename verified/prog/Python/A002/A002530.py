from functools import cache
@cache
def a(n): return [0, 1, 1, 3][n] if n < 4 else 4*a(n-2) - a(n-4)
print([a(n) for n in range(36)]) # _Michael S. Branicky_, Nov 13 2022