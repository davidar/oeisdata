A008506_list, m = [], [13, -65, 221, -494, 793, -923, 793, -494, 221, -65, 13, 0, 1]
for _ in range(10**2):
    A008506_list.append(m[-1])
    for i in range(12):
        m[i+1] += m[i] # _Chai Wah Wu_, Dec 15 2015
print(A008506_list)
