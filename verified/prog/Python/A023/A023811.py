def a(n): return (n**n - n**2 + n - 1)//((n - 1)**2) if n > 1 else 0
print([a(n) for n in range(1, 21)]) # _Michael S. Branicky_, Apr 24 2023