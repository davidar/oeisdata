A002109 = [1]
for n in range(1, 10):
    A002109.append(A002109[-1]*n**n) # _Chai Wah Wu_, Sep 03 2014
print(A002109)
