A029455_list, r = [], 0
for n in range(1,10**4+1):
    r = r*10**len(str(n))+n
    if not (r % n):
        A029455_list.append(n) # _Chai Wah Wu_, Nov 05 2014
print(A029455_list)
