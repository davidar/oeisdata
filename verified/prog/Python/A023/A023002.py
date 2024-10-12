A023002_list, m = [0], [3628800, -16329600, 30240000, -29635200, 16435440, -5103000, 818520, -55980, 1022, -1, 0 , 0]
for _ in range(20):
    for i in range(11):
        m[i+1]+= m[i]
    A023002_list.append(m[-1])
print(A023002_list) # _Chai Wah Wu_, Nov 05 2014