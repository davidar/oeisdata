def A002623(n): return ((n+2)*(n+4)*((n<<1)+3)>>3)//3 # _Chai Wah Wu_, Mar 25 2024
print([A002623(n) for n in range(30)])
