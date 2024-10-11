a, b = 14, 23
A010902_list = [a, b]
for i in range(1000):
    c, d = divmod(b**2, a)
    a, b = b, c + (0 if 2*d < a else 1)
    A010902_list.append(b) # _Chai Wah Wu_, Aug 08 2016
print(A010902_list)
