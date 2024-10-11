from functools import cache
@cache
def a(n): return n+1 if n < 4 else a(n//2) + a((n+1)//2)
print([a(n) for n in range(2, 72)]) # _Michael S. Branicky_, Aug 04 2022