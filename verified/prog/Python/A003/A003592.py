# A003592.py
from heapq import heappush, heappop
def A003592():
    pq = [1]
    seen = set(pq)
    while True:
        value = heappop(pq)
        yield value
        seen.remove(value)
        for x in 2*value, 5*value:
            if x not in seen:
                heappush(pq, x)
                seen.add(x)
sequence = A003592()
A003592_list = [next(sequence) for _ in range(100)]
print(A003592_list)
