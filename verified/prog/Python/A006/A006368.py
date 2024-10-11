def a(n): return 0 if n == 0 else 3*n//2 if n%2 == 0 else (3*n+1)//4
print([a(n) for n in range(72)]) # _Michael S. Branicky_, Aug 12 2021