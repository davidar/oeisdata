A017713_list, m = [], [1]*50
for _ in range(10**2):
    A017713_list.append(m[-1])
    for i in range(49):
        m[i+1] += m[i] # _Chai Wah Wu_, Jan 24 2016
print(A017713_list)
