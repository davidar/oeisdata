from re import split
def A014081(n): return sum(len(d)-1 for d in split('0+', bin(n)[2:]) if d != '') # _Chai Wah Wu_, Feb 04 2022
print([A014081(n) for n in range(30)])
