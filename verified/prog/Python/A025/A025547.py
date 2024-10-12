# generates initial segment of sequence
from math import gcd
from itertools import accumulate
def lcm(a, b): return a * b // gcd(a, b)
def aupton(nn): return list(accumulate((2*i+1 for i in range(nn)), lcm))
print(aupton(23)) # _Michael S. Branicky_, Mar 28 2022