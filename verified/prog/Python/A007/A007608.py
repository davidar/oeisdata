def A007608(n):
    s, q = '', n
    while q >= 4 or q < 0:
        q, r = divmod(q, -4)
        if r < 0:
            q += 1
            r += 4
        s += str(r)
    return int(str(q)+s[::-1]) # _Chai Wah Wu_, Apr 09 2016
print([A007608(n) for n in range(30)])
