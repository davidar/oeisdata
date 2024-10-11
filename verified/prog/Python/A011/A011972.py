from itertools import accumulate
A011972_list = blist = [1]
for _ in range(10**2):
    b = blist[-1]
    blist = list(accumulate([b]+blist))
    A011972_list += blist[1:]
# _Chai Wah Wu_, Sep 02 2014, updated _Chai Wah Wu_, Sep 20 2014
print(A011972_list)
