def A015521(n): return ((1<<(n<<1))|1)//5 # _Chai Wah Wu_, Jun 28 2023
print([A015521(n) for n in range(30)])
