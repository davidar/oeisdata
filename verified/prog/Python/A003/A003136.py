from itertools import count, islice
from sympy import factorint
def A003136_gen(): return (n for n in count(0) if all(e % 2 == 0 for p,e in factorint(n).items() if p % 3 == 2))
A003136_list = list(islice(A003136_gen(),30)) # _Chai Wah Wu_, Jan 20 2022
print(A003136_list)
