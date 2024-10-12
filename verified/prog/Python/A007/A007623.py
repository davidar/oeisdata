def a(n, p=2): return n if n<p else a(n//p, p+1)*10 + n%p
print([a(n - 1) for n in range(1, 201)]) # _Indranil Ghosh_, Jun 19 2017, after PARI program