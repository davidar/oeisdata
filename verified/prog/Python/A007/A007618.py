from itertools import accumulate
def f(an, _): return an + sum(int(d) for d in str(an))
print(list(accumulate([5]*55, f))) # _Michael S. Branicky_, May 10 2021