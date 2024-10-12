from itertools import islice
from collections import deque
def A022907_gen(): # generator of terms
    aqueue, f, b, a = deque([2]), True, 1, 2
    yield from (0, 2, 5)
    while True:
        a += b
        yield 3*a-1
        aqueue.append(a)
        if f: b = aqueue.popleft()
        f = not f
A022907_list = list(islice(A022907_gen(),40)) # _Chai Wah Wu_, Jun 08 2022
print(A022907_list)
