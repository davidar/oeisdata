A027603_list, m = [], [24, 12, 28, 36]
for _ in range(10**2):
    A027603_list.append(m[-1])
    for i in range(3):
        m[i+1] += m[i] # _Chai Wah Wu_, Dec 15 2015
print(A027603_list)
