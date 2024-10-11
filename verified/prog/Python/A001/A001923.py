# generates initial segment of sequence
from itertools import accumulate
def f(k): return 0 if k == 0 else k**k
def aupton(nn): return list(accumulate(f(k) for k in range(nn+1)))
print(aupton(17)) # _Michael S. Branicky_, Feb 12 2022