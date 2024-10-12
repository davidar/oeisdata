from itertools import islice
from collections import deque
def A022908_gen(): # generator of terms
    aqueue, f, b, a = deque([2]), True, 1, 2
    yield from (0,2)
    while True:
        a += b
        aqueue.append(a)
        if f:
            yield (3*a+1)//2
            b = aqueue.popleft()
        f = not f
A022908_list = list(islice(A022908_gen(),40)) # _Chai Wah Wu_, Jun 08 2022
print(A022908_list)
