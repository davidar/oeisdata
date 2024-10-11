A002708_list, a, b, = [], 1, 1
for n in range(1,10**4+1):
    A002708_list.append(a%n)
    a, b = b, a+b # _Chai Wah Wu_, Nov 26 2015
print(A002708_list)
