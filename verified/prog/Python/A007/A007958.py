def ok(n): return n%2 == 0 and set(str(n)) & set("13579") != set()
print(list(filter(ok, range(163)))) # _Michael S. Branicky_, Oct 12 2021