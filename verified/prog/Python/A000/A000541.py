A000541_list, m = [0], [5040, -15120, 16800, -8400, 1806, -126, 1, 0, 0]
for _ in range(10**2):
    for i in range(8):
        m[i+1] += m[i]
    A000541_list.append(m[-1]) # _Chai Wah Wu_, Nov 05 2014
print(A000541_list)
