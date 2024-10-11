# generates initial segment of sequence
from math import gcd
from itertools import accumulate
def lcm(a, b): return a * b // gcd(a, b)
def aupton(nn): return [1] + list(accumulate(range(1, nn+1), lcm))
print(aupton(30)) # _Michael S. Branicky_, Jun 10 2021