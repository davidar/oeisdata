from itertools import count, islice
from sympy.ntheory.factor_ import digits
def A003137_gen(): return (d for m in count(1) for d in digits(m,3)[1:])
A003137_list = list(islice(A003137_gen(),30)) # _Chai Wah Wu_, Jan 07 2022
print(A003137_list)
