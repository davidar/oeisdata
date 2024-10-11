A003098_list = [m for m in (n*(n+1)//2 for n in range(10**5)) if str(m) == str(m)[::-1]] # _Chai Wah Wu_, Sep 03 2021
print(A003098_list)
