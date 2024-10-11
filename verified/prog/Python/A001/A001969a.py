def ok(n): return bin(n)[2:].count('1') % 2 == 0
print(list(filter(ok, range(130)))) # _Michael S. Branicky_, Jun 02 2021