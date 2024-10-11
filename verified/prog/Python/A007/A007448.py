def aupton(nn):
    alst = [1]
    [alst.append(1 + min(2*alst[n//2], 3*alst[n//3])) for n in range(nn)]
    return alst
print(aupton(70)) # _Michael S. Branicky_, Mar 28 2022