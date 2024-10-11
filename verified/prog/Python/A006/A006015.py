def a(n, D=[0, 2, 3, 1]):
    r, k = 0, 0
    while n>0: r+=D[n%4]*4**k; n//=4; k+=1
    return r
# _Onur Ozkan_, Mar 07 2023
print([a(n) for n in range(30)])
