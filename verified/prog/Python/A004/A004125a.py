def a(n): return sum(n%k for k in range(1, n))
print([a(n) for n in range(1, 63)]) # _Michael S. Branicky_, Jun 08 2021