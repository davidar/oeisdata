A005917_list, m = [], [24, -12, 2, 1]
for _ in range(10**2):
    A005917_list.append(m[-1])
    for i in range(3):
        m[i+1] += m[i] # _Chai Wah Wu_, Dec 15 2015
print(A005917_list)
