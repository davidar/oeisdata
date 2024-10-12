from itertools import count
def A023183(n):
    if n < 2: return n
    if n > 99 and n%8 in {4, 6}: return -1
    k, f, g, s = 3, 1, 2, str(n)
    pow10, seen = 10**len(s), set()
    while (f, g) not in seen:
        seen.add((f, g))
        if g%pow10 == n:
            return k
        f, g, k = g, (f+g)%pow10, k+1
    return -1
print([A023183(n) for n in range(66)]) # _Michael S. Branicky_, Jun 27 2024