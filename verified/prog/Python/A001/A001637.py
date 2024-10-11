def a(n): return n + (100**((len(str(110*n))-1)//2) - 1)//11
print([a(n) for n in range(1, 100)]) # _Michael S. Branicky_, Nov 10 2022 after _Kevin Ryde_