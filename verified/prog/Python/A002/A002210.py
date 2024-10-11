from mpmath import mp, khinchin
mp.dps = 106
print([int(k) for k in list(str(khinchin).replace('.', ''))[:-1]]) # _Indranil Ghosh_, Jul 08 2017