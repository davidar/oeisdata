from itertools import groupby
def A004718(n):
    c = 0
    for k, g in groupby(bin(n)[2:]):
        c = c+len(list(g)) if k == '1' else (-c if len(list(g))&1 else c)
    return c # _Chai Wah Wu_, Mar 02 2023
print([A004718(n) for n in range(30)])
