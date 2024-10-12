def ok(n): return sorted(str(n)) == sorted(str(2*n))
print(list(filter(ok, range(1087543)))) # _Michael S. Branicky_, May 21 2021