A000538_list, m = [0], [24, -36, 14, -1, 0, 0]
for _ in range(10**2):
    for i in range(5):
        m[i+1] += m[i]
    A000538_list.append(m[-1]) # _Chai Wah Wu_, Nov 05 2014
print(A000538_list)
