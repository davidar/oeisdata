def A005351(n):
    s, q = '', n
    while q >= 2 or q < 0:
        q, r = divmod(q, -2)
        if r < 0:
            q += 1
            r += 2
        s += str(r)
    return int(str(q)+s[::-1],2) # _Chai Wah Wu_, Apr 10 2016
print([A005351(n) for n in range(30)])
