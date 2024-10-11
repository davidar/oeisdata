def aupton(nn):
    alst = [1, 0, 0]
    for n in range(3, nn+1): alst.append(alst[n-2]+alst[n-3])
    return alst
print(aupton(49)) # _Michael S. Branicky_, Mar 28 2022