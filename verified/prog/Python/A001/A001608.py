A001608_list, a, b, c = [3, 0, 2], 3, 0, 2
for _ in range(100):
    a, b, c = b, c, a+b
    A001608_list.append(c) # _Chai Wah Wu_, Jan 27 2015
print(A001608_list)
