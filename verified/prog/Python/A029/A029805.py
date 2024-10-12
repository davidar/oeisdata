from itertools import count, islice
def A029805_gen(): # generator of terms
    return filter(lambda k: (s:=oct(k**2)[2:])[:(t:=(len(s)+1)//2)]==s[:-t-1:-1],count(0))
A029805_list = list(islice(A029805_gen(),20)) # _Chai Wah Wu_, Jun 23 2022
print(A029805_list)
