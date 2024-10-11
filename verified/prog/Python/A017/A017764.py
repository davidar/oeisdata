A017764_list, m = [], [1]*101
for _ in range(10**2):
    A017764_list.append(m[-1])
    for i in range(100):
        m[i+1] += m[i] # _Chai Wah Wu_, Jan 24 2016
print(A017764_list)
