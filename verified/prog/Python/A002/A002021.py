def a(n): return (n-1)*(n**n - 1) if n%2 == 0 else n**n - n + 1
print([a(n) for n in range(1, 20)]) # _Michael S. Branicky_, Feb 07 2022