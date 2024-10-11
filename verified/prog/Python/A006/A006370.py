def A006370(n):
    q, r = divmod(n, 2)
    return 3*n+1 if r else q # _Chai Wah Wu_, Jan 04 2015
print([A006370(n) for n in range(30)])
