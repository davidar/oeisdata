from functools import lru_cache
@lru_cache(maxsize=None)
def A008336(n):
    if n == 1: return 1
    a, b = divmod(c:=A008336(n-1),n-1)
    return c*(n-1) if b else a # _Chai Wah Wu_, Apr 11 2024
print([A008336(n) for n in range(1,31)])
