A008863_list, m = [], [1, -8, 29, -62, 86, -80, 50, -20, 5, 0, 1]
for _ in range(10**2):
    A008863_list.append(m[-1])
    for i in range(10):
        m[i+1] += m[i] # _Chai Wah Wu_, Jan 24 2016
print(A008863_list)
