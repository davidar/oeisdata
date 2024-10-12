from collections import Counter
def A025591(n):
    c = {0:1,1:1}
    for i in range(2,n+1):
        d = Counter(c)
        for k in c:
            d[k+i] += c[k]
        c = d
    return max(c.values()) # _Chai Wah Wu_, Jan 31 2024
print([A025591(n) for n in range(30)])
