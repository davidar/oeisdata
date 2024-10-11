def a(n): return int(bin(n)[2:]*2, 2)
print([a(n) for n in range(1, 51)]) # _Michael S. Branicky_, Mar 10 2021