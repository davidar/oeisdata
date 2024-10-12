from itertools import permutations
A023804_list = sorted(set(int(''.join(d),9) for k in range(1,10) for d in permutations('012345678',k))) # _Chai Wah Wu_, Mar 25 2021
print(A023804_list)
