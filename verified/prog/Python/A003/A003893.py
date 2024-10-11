A003893_list, a, b, = [], 0, 1
for _ in range(10**3):
    A003893_list.append(a)
    a, b = b, (a+b) % 10 # _Chai Wah Wu_, Nov 26 2015
print(A003893_list)
