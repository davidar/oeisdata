A000578_list, m = [], [6, -6, 1, 0]
for _ in range(10**2):
    A000578_list.append(m[-1])
    for i in range(3):
        m[i+1] += m[i] # _Chai Wah Wu_, Dec 15 2015
print(A000578_list)
