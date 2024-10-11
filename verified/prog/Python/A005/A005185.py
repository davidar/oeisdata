from functools import lru_cache
@lru_cache(maxsize=None)
def a(n):
    if n < 3: return 1
    return a(n - a(n-1)) + a(n - a(n-2))
print([a(n) for n in range(1, 75)]) # _Michael S. Branicky_, Jul 26 2021