def a(n): return (int(bin(n>>1)[2:])<<1)+(n&1)
print([a(n) for n in range(50)]) # _Michael S. Branicky_, Aug 06 2023