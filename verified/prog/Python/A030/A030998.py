from itertools import count, chain, islice
from sympy.ntheory.factor_ import digits
def A030998_gen(): return chain.from_iterable(digits(m, 7)[1:] for m in count(0))
A030998_list = list(islice(A030998_gen(), 30)) # _Chai Wah Wu_, Jan 07 2022
print(A030998_list)
