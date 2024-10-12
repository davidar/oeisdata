from itertools import count, chain, islice
from sympy.ntheory.factor_ import digits
def A030373_gen(): return chain.from_iterable(digits(m, 4)[1:] for m in count(1))
A030373_list = list(islice(A030373_gen(), 30)) # _Chai Wah Wu_, Jan 07 2022
print(A030373_list)
