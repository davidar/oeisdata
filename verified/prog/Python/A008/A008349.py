A008349_list, m = [], [328320, -1071360, 1347840, -812160, 233280, -25920, 240, 0, 1]
for _ in range(10**2):
    A008349_list.append(m[-1])
    for i in range(8):
        m[i+1] += m[i] # _Chai Wah Wu_, Dec 15 2015
print(A008349_list)
