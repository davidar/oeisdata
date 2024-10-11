A000579_list, m = [], [1, -5, 10, -10, 5, -1, 0]
for _ in range(10**2):
    A000579_list.append(m[-1])
    for i in range(6):
        m[i+1] += m[i] # _Chai Wah Wu_, Jan 24 2016
print(A000579_list)
