A000540_list, m = [0], [720, -1800, 1560, -540, 62, -1, 0, 0]
for _ in range(10**2):
    for i in range(7):
        m[i+1] += m[i]
    A000540_list.append(m[-1]) # _Chai Wah Wu_, Nov 05 2014
print(A000540_list)
