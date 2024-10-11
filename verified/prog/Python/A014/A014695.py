def A014695(n): return (1,2,2,1)[n&3] # _Chai Wah Wu_, Apr 17 2023
print([A014695(n) for n in range(30)])
