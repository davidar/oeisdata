# without string operations
def a(n): return 0 if n == 0 else (10**((n-1)//9+1)-1)//9*((n-1)%9+1)
print([a(n) for n in range(55)]) # _Michael S. Branicky_, Nov 03 2023