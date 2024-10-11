from mpmath import mp, agm, sqrt
mp.dps=105
print([int(z) for z in list(str(1/agm(sqrt(2)))[2:-1])]) # _Indranil Ghosh_, Jul 11 2017