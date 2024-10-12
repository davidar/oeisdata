def aupto(N):
    alst = []
    for i in range(1, N-1):
        for j in range(i+1, N//i + 1):
            p, s = i*j, i+j
            for k in range(j+1, (N-p)//s + 1):
                alst.append(p + s*k)
    return sorted(alst)
print(aupto(65)) # _Michael S. Branicky_, Nov 14 2021