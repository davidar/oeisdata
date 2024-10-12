from itertools import islice
from collections import deque
def A022905_gen(): # generator of terms
    aqueue, f, b, a = deque([2]), True, 1, 2
    yield 1
    while True:
        a += b
        aqueue.append(a)
        if f:
            yield (3*a-1)//2
            b = aqueue.popleft()
        f = not f
A022905_list = list(islice(A022905_gen(),40)) # _Chai Wah Wu_, Jun 08 2022
print(A022905_list)
