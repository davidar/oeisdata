import math
from mpmath import *
mp.dps = 100
print([n + sum([int(math.floor((n - k)/pi)) for k in range(1, n + 1)]) for n in range(1, 101)]) # _Indranil Ghosh_, May 28 2019