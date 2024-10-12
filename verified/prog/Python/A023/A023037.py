def A023037(n): return (n**n-1)//(n-1) if n>1 else n # _Chai Wah Wu_, Sep 28 2023
print([A023037(n) for n in range(30)])
