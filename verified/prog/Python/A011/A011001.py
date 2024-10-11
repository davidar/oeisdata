A011001_list, m = [], [1]*49
for _ in range(10**2):
    A011001_list.append(m[-1])
    for i in range(48):
        m[i+1] += m[i] # _Chai Wah Wu_, Jan 24 2016
print(A011001_list)
