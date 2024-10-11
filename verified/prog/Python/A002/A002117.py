from mpmath import mp, apery
mp.dps=109
print([int(z) for z in list(str(apery).replace('.', ''))[:-1]]) # _Indranil Ghosh_, Jul 08 2017