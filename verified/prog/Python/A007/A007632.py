from itertools import chain
A007632_list = sorted([n for n in chain((int(str(x)+str(x)[::-1]) for x in range(1,10**6)),(int(str(x)+str(x)[-2::-1]) for x in range(10**6))) if bin(n)[2:] == bin(n)[:1:-1]]) # _Chai Wah Wu_, Nov 23 2014
print(A007632_list)
