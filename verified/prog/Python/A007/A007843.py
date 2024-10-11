from itertools import count
def A007843(n):
    c = 0
    for k in count(1):
        c += (~k&k-1).bit_length()
        if c >= n:
            return k # _Chai Wah Wu_, Jul 08 2022
print([A007843(n) for n in range(30)])
