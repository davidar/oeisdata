def O(f):
    c = 1
    while len(f) > 1:
        f.sort()
        m = abs(f[0] - f[1])
        c *= m
        f[0] = m
        f.pop(1)
    return c
a = lambda n: O(list(range(1, n+1)))
print([a(n) for n in range(0, 26)]) # _Darío Clavijo_, Aug 24 2024