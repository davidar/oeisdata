from itertools import count, islice
def A002778_gen(): # generator of terms
    return filter(lambda k: (s:=str(k**2))[:(t:=(len(s)+1)//2)]==s[:-t-1:-1],count(0))
A002778_list = list(islice(A002778_gen(),20)) # _Chai Wah Wu_, Jun 23 2022
print(A002778_list)
