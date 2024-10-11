def a(n): return 0 if n == 0 else int(str((n-1)%9+1)*((n-1)//9+1))
print([a(n) for n in range(55)]) # _Michael S. Branicky_, Dec 29 2021