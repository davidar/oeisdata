from itertools import count, chain, islice
from sympy.ntheory.factor_ import digits
def A030548_gen(): return chain.from_iterable(digits(m, 6)[1:] for m in count(1))
A030548_list = list(islice(A030548_gen(), 30)) # _Chai Wah Wu_, Jan 07 2022
print(A030548_list)
