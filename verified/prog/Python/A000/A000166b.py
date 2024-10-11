A000166_list, m, x = [], 1, 1
for n in range(10*2):
    x, m = x*n + m, -m
    A000166_list.append(x) # _Chai Wah Wu_, Nov 03 2014
print(A000166_list)
