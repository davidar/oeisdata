from itertools import chain, count, islice
def A029803_gen(): # generator of terms
    return chain((0,),chain.from_iterable(chain((int((s:=oct(d)[2:])+s[-2::-1],8) for d in range(8**l,8**(l+1))), (int((s:=oct(d)[2:])+s[::-1],8) for d in range(8**l,8**(l+1)))) for l in count(0)))
A029803_list = list(islice(A029803_gen(),20)) # _Chai Wah Wu_, Jun 23 2022
print(A029803_list)
