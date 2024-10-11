from itertools import accumulate
def f(anm1, _): return anm1**2 - 2
print(list(accumulate([4]*8, f))) # _Michael S. Branicky_, Apr 14 2021