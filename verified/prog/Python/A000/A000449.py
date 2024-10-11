A000449_list, m, x = [], 1, 0
for n in range(3,21):
    x, m = x*n + m*(n*(n-1)*(n-2)//6), -m
    A000449_list.append(x) # _Chai Wah Wu_, Sep 23 2014
print(A000449_list)
