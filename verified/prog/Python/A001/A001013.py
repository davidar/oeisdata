def aupto(lim, mx=None):
    if lim < 2: return [1]
    v, t = [1], 1
    if mx == None: mx = lim
    for k in range(2, mx+1):
        t *= k
        if t > lim: break
        v += [t*rest for rest in aupto(lim//t, t)]
    return sorted(set(v))
print(aupto(5760)) # _Michael S. Branicky_, Jul 21 2021 after _Charles R Greathouse IV_