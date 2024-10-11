def ok(n): return '0' not in str(2**n)
print(list(filter(ok, range(10**4)))) # _Michael S. Branicky_, Aug 08 2021