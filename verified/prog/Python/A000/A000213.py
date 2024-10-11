alst = [1, 1, 1]
[alst.append(alst[n-1] + alst[n-2] + alst[n-3]) for n in range(3, 37)]
print(alst) # _Michael S. Branicky_, Sep 21 2021