A002419_list, m = [], [6, 1, 1, 1, 1]
for _ in range(10**2):
    A002419_list.append(m[-1])
    for i in range(4):
        m[i+1] += m[i] # _Chai Wah Wu_, Jan 24 2016
print(A002419_list)
