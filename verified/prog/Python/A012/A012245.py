from itertools import count
def A012245(n):
    c = 1
    for i in count(1):
        if (c:=c*i) >= n:
            return int(c==n) # _Chai Wah Wu_, Jan 11 2023
print([A012245(n) for n in range(1,31)])
