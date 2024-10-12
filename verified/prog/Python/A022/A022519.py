from itertools import groupby
A022519_list = [8]
for _ in range(10):
    A022519_list.append(int(''.join(str(k)+str(len(list(g))) for k, g in groupby(str(A022519_list[-1])[::-1])))) # _Chai Wah Wu_, Sep 01 2021
print(A022519_list)
