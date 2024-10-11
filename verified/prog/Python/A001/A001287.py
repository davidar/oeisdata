A001287_list, m = [], [1]*11
for _ in range(10**2):
    A001287_list.append(m[-1])
    for i in range(10):
        m[i+1] += m[i] # _Chai Wah Wu_, Jan 24 2016
print(A001287_list)
