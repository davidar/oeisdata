from itertools import chain
A002113 = sorted(chain(map(lambda x:int(str(x)+str(x)[::-1]),range(1,10**3)),map(lambda x:int(str(x)+str(x)[-2::-1]), range(10**3)))) # _Chai Wah Wu_, Aug 09 2014
print(A002113)
