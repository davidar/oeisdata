A017714_list, m = [], [1]*51
for _ in range(10**2):
    A017714_list.append(m[-1])
    for i in range(50):
        m[i+1] += m[i] # _Chai Wah Wu_, Jan 24 2016
print(A017714_list)
