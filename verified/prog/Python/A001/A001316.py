def A001316(n):
    return 2**bin(n)[2:].count("1") # _Indranil Ghosh_, Feb 06 2017
print([A001316(n) for n in range(30)])
