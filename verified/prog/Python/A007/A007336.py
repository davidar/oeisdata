from bisect import bisect
from collections import defaultdict
from functools import cache
from math import ceil
memos = defaultdict(lambda: [-1, 0])
@cache
def zero_based_c(theta, i):
    memo = memos[theta]
    while memo[-1] <= i:
        memo.append(memo[-1] + ceil(theta * (len(memo) - 1)))
    depth = bisect(memo, i) - 1
    return 0 if depth > i or memo[depth] == i else 1 + zero_based_c(theta, i - depth)
def A007336(i):
    return zero_based_c(2 ** 0.5, i - 1) + 1
print([A007336(i) for i in range(1, 1001)])  # _Brady J. Garvin_, Aug 18 2024