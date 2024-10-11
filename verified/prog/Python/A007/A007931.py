def a(n): return int(bin(n+1)[3:].replace('1', '2').replace('0', '1'))
print([a(n) for n in range(1, 45)]) # _Michael S. Branicky_, May 13 2021