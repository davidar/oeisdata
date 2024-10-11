from itertools import combinations_with_replacement as mc
def aupto(lim):
    cbs = (i**3 for i in range(1, int((lim-7)**(1/3))+2))
    return sorted(set(k for k in (sum(c) for c in mc(cbs, 8)) if k <= lim))
print(aupto(150)) # _Michael S. Branicky_, Aug 15 2021