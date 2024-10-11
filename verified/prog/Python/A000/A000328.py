def A000328(n):
    return (sum([int((n**2 - y**2)**0.5) for y in range(1, n)]) * 4 + 4*n + 1)
    # _Karl-Heinz Hofmann_, Aug 03 2022
print([A000328(n) for n in range(30)])
