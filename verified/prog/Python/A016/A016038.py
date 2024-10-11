from itertools import count, islice
from sympy.ntheory.factor_ import digits
def A016038_gen(startvalue=0): # generator of terms >= startvalue
    return filter(lambda n: all((s := digits(n,b)[1:])[:(t:=len(s)+1>>1)]!=s[:-t-1:-1] for b in range(2,n-1)), count(max(startvalue,0)))
A016038_list = list(islice(A016038_gen(),30)) # _Chai Wah Wu_, Jan 17 2024
print(A016038_list)
