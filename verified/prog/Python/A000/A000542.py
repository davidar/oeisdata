A000542_list, m = [0], [40320, -141120, 191520, -126000, 40824, -5796, 254, -1, 0, 0]
for _ in range(24):
    for i in range(9):
        m[i+1] += m[i]
    A000542_list.append(m[-1])
print(A000542_list) # _Chai Wah Wu_, Nov 05 2014