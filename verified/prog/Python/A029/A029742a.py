def ok(n): s = str(n); return s != s[::-1]
print(list(filter(ok, range(108)))) # _Michael S. Branicky_, Oct 12 2021