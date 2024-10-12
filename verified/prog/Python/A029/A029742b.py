def A029742(n):
    def f(x): return n+x//10**((l:=len(s:=str(x)))-(k:=l+1>>1))-(int(s[k-1::-1])>x%10**k)+10**(k-1+(l&1^1))-1
    m, k = n, f(n)
    while m != k:
        m, k = k, f(k)
    return m # _Chai Wah Wu_, Jul 24 2024
print([A029742(n) for n in range(1,31)])
