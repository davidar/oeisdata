def A028356(n): return (1,2,3,4,3,2)[n%6] # _Chai Wah Wu_, Apr 18 2024
print([A028356(n) for n in range(30)])
