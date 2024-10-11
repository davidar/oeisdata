A000539_list, m = [0], [120, -240, 150, -30, 1, 0, 0]
for _ in range(10**2):
    for i in range(6):
        m[i+1] += m[i]
    A000539_list.append(m[-1]) # _Chai Wah Wu_, Nov 05 2014
print(A000539_list)
