from itertools import accumulate, repeat # requires Python 3.2 or higher
from sympy import divisor_sigma
A007497_list = list(accumulate(repeat(2,100), lambda x, _: divisor_sigma(x)))
# _Chai Wah Wu_, May 02 2015
print(A007497_list)
