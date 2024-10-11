from math import isqrt
from itertools import count, islice
def A003233_gen(startvalue=1): # generator of terms >= startvalue
    return filter(lambda n:((m:=(n+isqrt(5*n**2)>>1)+n)+isqrt(5*m**2)>>1)+(m<<1)==((k:=(n+isqrt(5*n**2)>>1)+(n<<1))+isqrt(5*k**2)>>1)+k,count(max(1,startvalue)))
A003233_list = list(islice(A003233_gen(),30)) # _Chai Wah Wu_, Sep 02 2022
print(A003233_list)
