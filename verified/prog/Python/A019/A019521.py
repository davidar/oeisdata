def a(n): return int("".join(str(i*i) for i in range(1, n+1)))
print([a(n) for n in range(1, 16)]) # _Michael S. Branicky_, Jan 14 2021