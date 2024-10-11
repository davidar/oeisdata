def ok(n): return pow(2, n, n) == 2%n
print([k for k in range(1, 400) if ok(k)]) # _Michael S. Branicky_, Jun 03 2022