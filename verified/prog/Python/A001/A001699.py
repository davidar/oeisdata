from functools import lru_cache
@lru_cache(maxsize=None)
def a(n): return 1 if n <= 1 else a(n-1) * (a(n-1) + a(n-2) + a(n-1)//a(n-2))
print([a(n) for n in range(10)]) # _Michael S. Branicky_, Nov 10 2022 after _Michael Somos_