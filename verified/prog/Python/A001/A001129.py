A001129_list, r1, r2 = [0,1], 1, 0
for _ in range(10**2):
    l, r2 = r1+r2, r1
    r1 = int(str(l)[::-1])
    A001129_list.append(l) # _Chai Wah Wu_, Jan 03 2015
print(A001129_list)
