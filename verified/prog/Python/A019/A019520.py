def a(n): return int("".join(str(2*i) for i in range(1, n+1)))
print([a(n) for n in range(1, 17)]) # _Michael S. Branicky_, Dec 18 2021