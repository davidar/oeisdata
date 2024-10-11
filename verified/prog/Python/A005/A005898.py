A005898_list, m = [], [12, -6, 2, 1]
for _ in range(10**2):
    A005898_list.append(m[-1])
    for i in range(3):
        m[i+1] += m[i] # _Chai Wah Wu_, Dec 15 2015
print(A005898_list)
