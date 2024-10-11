def a(n):
    s=1
    while True:
        ns=n>>s
        if ns==0: break
        n=n^ns
        s<<=1
    return n
print([a(n) for n in range(101)]) # _Indranil Ghosh_, Jun 07 2017, after PARI code by _Joerg Arndt_