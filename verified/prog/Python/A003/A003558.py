def A003558(n):
    m, k = 1, 2 % (c:=(r:=n<<1)+1)
    while not (k==1 or k==r):
        k = 2*k%c
        m += 1
    return m # _Chai Wah Wu_, Oct 09 2023
print([A003558(n) for n in range(30)])
