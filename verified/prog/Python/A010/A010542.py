from math import isqrt
def aupton(nn): return list(map(int, str(isqrt(91 * 10**(2*nn)))))[:nn]
print(aupton(100)) # _Michael S. Branicky_, Sep 05 2021