def aupton(terms):
    alst = [9]
    for n in range(2, terms+1): alst.append(int(oct(alst[-1])[2:]))
    return alst
print(aupton(35)) # _Michael S. Branicky_, Sep 11 2021